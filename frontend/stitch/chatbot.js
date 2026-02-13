/**
 * CareerLens AI - Shared Chatbot Intelligence
 * Centralized logic for the floating AI Advisor
 */

class CareerLensChatbot {
    constructor() {
        this.fab = document.getElementById('chatbotFab');
        this.window = document.getElementById('chatbotWindow');
        this.closeBtn = document.getElementById('closeChat');
        this.form = document.getElementById('chatForm');
        this.input = document.getElementById('chatInput');
        this.messages = document.getElementById('chatMessages');
        this.suggestionGrid = document.getElementById('chatbotSuggestions');

        this.isProcessing = false;
        this.historyKey = 'career_chat_history';

        this.init();
    }

    init() {
        if (!this.fab) return;

        // Toggle Window
        this.fab.addEventListener('click', () => {
            this.window.classList.toggle('hidden');
            if (!this.window.classList.contains('hidden')) {
                this.input.focus();
                this.scrollToBottom();
            }
        });

        this.closeBtn?.addEventListener('click', () => this.window.classList.add('hidden'));

        // Form Submit
        this.form?.addEventListener('submit', (e) => {
            e.preventDefault();
            this.handleUserAction(this.input.value);
        });

        // Load History
        this.loadHistory();
        this.renderSuggestions();
    }

    async handleUserAction(message) {
        if (!message.trim() || this.isProcessing) return;

        const userMsg = message.trim();
        this.input.value = '';
        this.addMessage(userMsg, 'user');
        this.saveToHistory(userMsg, 'user');

        await this.getAIResponse(userMsg);
    }

    async getAIResponse(message) {
        this.isProcessing = true;
        const loadingId = this.addLoadingIndicator();

        try {
            const apiHost = window.location.hostname || '127.0.0.1';
            const context = this.getCareerContext();

            const response = await fetch(`http://${apiHost}:9000/api/chatbot`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message, context })
            });

            const data = await response.json();
            this.removeLoadingIndicator(loadingId);

            const aiResponse = data.response || "I'm sorry, I couldn't process that.";
            this.addMessage(aiResponse, 'ai');
            this.saveToHistory(aiResponse, 'ai');

        } catch (err) {
            this.removeLoadingIndicator(loadingId);
            this.addMessage("Connection failed. Is the backend server running?", 'ai');
        } finally {
            this.isProcessing = false;
        }
    }

    getCareerContext() {
        // Pull latest analysis from localStorage
        const analysis = JSON.parse(localStorage.getItem('careerAnalysis') || '{}');
        const history = JSON.parse(localStorage.getItem('careerAnalysisHistory') || '[]');

        return {
            role: analysis.target_role || (history[0] ? history[0].target_role : 'Career Explorer'),
            score: analysis.gap_analysis ? analysis.gap_analysis.match_score : 'N/A',
            missing_skills: analysis.gap_analysis ? analysis.gap_analysis.missing_skills.slice(0, 5) : []
        };
    }

    addMessage(text, type) {
        const div = document.createElement('div');
        div.className = type === 'user' ? 'flex justify-end' : 'flex gap-3 max-w-[85%]';

        if (type === 'user') {
            div.innerHTML = `
                <div class="bg-primary text-background-dark px-4 py-2.5 rounded-2xl rounded-tr-none text-xs font-bold shadow-lg">
                    ${text}
                </div>
            `;
        } else {
            div.innerHTML = `
                <div class="size-8 rounded-lg bg-primary/10 flex items-center justify-center shrink-0">
                    <span class="material-symbols-outlined text-primary text-xs">psychology</span>
                </div>
                <div class="bg-white/5 border border-white/5 p-4 rounded-2xl rounded-tl-none text-xs leading-relaxed text-slate-300 shadow-sm">
                    ${text.replace(/\n/g, '<br>')}
                </div>
            `;
        }

        this.messages.appendChild(div);
        this.scrollToBottom();
    }

    addLoadingIndicator() {
        const id = 'loading_' + Date.now();
        const div = document.createElement('div');
        div.id = id;
        div.className = 'flex gap-3 max-w-[85%] animate-pulse';
        div.innerHTML = `
            <div class="size-8 rounded-lg bg-primary/10 flex items-center justify-center shrink-0">
                <span class="material-symbols-outlined text-primary text-xs">smart_toy</span>
            </div>
            <div class="bg-white/5 p-3 rounded-2xl italic text-[10px] text-slate-500">
                AI Advisor is thinking...
            </div>
        `;
        this.messages.appendChild(div);
        this.scrollToBottom();
        return id;
    }

    removeLoadingIndicator(id) {
        document.getElementById(id)?.remove();
    }

    scrollToBottom() {
        this.messages.scrollTop = this.messages.scrollHeight;
    }

    renderSuggestions() {
        if (!this.suggestionGrid) return;

        const suggestions = [
            "How to improve my score?",
            "Project ideas for Java",
            "Prepare for interview",
            "What's my biggest gap?"
        ];

        this.suggestionGrid.innerHTML = suggestions.map(s => `
            <button class="bg-white/5 hover:bg-primary/20 border border-white/10 rounded-full px-3 py-1.5 text-[10px] text-slate-400 hover:text-primary transition-all whitespace-nowrap"
                    onclick="window.careerChatbot.handleUserAction('${s}')">
                ${s}
            </button>
        `).join('');
    }

    saveToHistory(text, type) {
        const history = JSON.parse(localStorage.getItem(this.historyKey) || '[]');
        history.push({ text, type, time: Date.now() });
        if (history.length > 30) history.shift();
        localStorage.setItem(this.historyKey, JSON.stringify(history));
    }

    loadHistory() {
        const history = JSON.parse(localStorage.getItem(this.historyKey) || '[]');
        if (history.length === 0) return;

        this.messages.innerHTML = ''; // Start fresh
        history.forEach(item => this.addMessage(item.text, item.type));
    }
}

// Global Instance
window.addEventListener('DOMContentLoaded', () => {
    window.careerChatbot = new CareerLensChatbot();
});
