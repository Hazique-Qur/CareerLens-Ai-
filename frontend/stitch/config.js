/**
 * CareerLens AI — Global Configuration
 * 
 * On Vercel, frontend & backend share the same domain,
 * so deployed API calls use relative URLs (empty string).
 * Local development uses localhost:9000.
 */

const CAREERLENS_CONFIG = (() => {
    const isLocal = ["localhost", "127.0.0.1", ""].includes(window.location.hostname)
        || window.location.protocol === "file:";

    const API_BASE = isLocal
        ? "http://127.0.0.1:9000"
        : "";  // Same domain on Vercel — relative URLs work!

    return { API_BASE };
})();
