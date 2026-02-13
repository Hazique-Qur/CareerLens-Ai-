/**
 * CareerLens AI — Global Configuration
 * 
 * UPDATE THE RENDER_URL BELOW after deploying the backend on Render.
 * Local development uses localhost:9000 automatically.
 */

const CAREERLENS_CONFIG = (() => {
    // ⬇️ PASTE YOUR RENDER BACKEND URL HERE (e.g., "https://career-lens-ai.onrender.com")
    const RENDER_URL = "";

    const isLocal = ["localhost", "127.0.0.1", ""].includes(window.location.hostname)
        || window.location.protocol === "file:";

    const API_BASE = isLocal
        ? "http://127.0.0.1:9000"
        : (RENDER_URL || "http://127.0.0.1:9000");

    return { API_BASE };
})();
