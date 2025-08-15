const CACHE_NAME = "thinkbright-cache-v2";

// Install and cache all current files automatically
self.addEventListener("install", event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            return fetch("manifest.json")
                .then(() => cache.addAll([
                    "./",
                    "./index.html",
                    "./manifest.json"
                ]))
                .catch(() => {
                    return cache.addAll(["./", "./index.html"]);
                });
        })
    );
    self.skipWaiting();
});

// Fetch from cache first, then fallback to network
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request).then(networkResponse => {
                return caches.open(CACHE_NAME).then(cache => {
                    cache.put(event.request, networkResponse.clone());
                    return networkResponse;
                });
            }).catch(() => {
                return caches.match("./index.html");
            });
        })
    );
});

// Activate new service worker and delete old caches
self.addEventListener("activate", event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(name => name !== CACHE_NAME)
                    .map(name => caches.delete(name))
            );
        })
    );
    self.clients.claim();
});