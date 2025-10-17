// Main JavaScript file for T2V Bot

// Utility function to show notifications
function showNotification(message, type = 'info') {
    // This is a simple console log for now
    // In production, you'd want to use a proper notification system
    console.log(`[${type.toUpperCase()}] ${message}`);
}

// Function to format dates
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleString();
}

// Function to validate text input
function validateTextPrompt(text) {
    if (!text || text.trim().length === 0) {
        return { valid: false, message: 'Please enter a text prompt' };
    }
    if (text.trim().length < 10) {
        return { valid: false, message: 'Prompt should be at least 10 characters long' };
    }
    return { valid: true };
}

// Initialize application
document.addEventListener('DOMContentLoaded', function() {
    console.log('T2V Bot initialized');
    
    // Add any initialization code here
    // For example, checking if Ollama is available
    checkOllamaStatus();
});

// Check if Ollama API is available
async function checkOllamaStatus() {
    try {
        // This is a placeholder - in production, you'd ping the Ollama API
        console.log('Checking Ollama API status...');
        // You could add a visual indicator of Ollama status on the page
    } catch (error) {
        console.warn('Ollama API check failed:', error);
    }
}

// Export functions for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        showNotification,
        formatDate,
        validateTextPrompt
    };
}
