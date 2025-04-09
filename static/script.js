async function translateText() {
    const text = document.getElementById("text-input").value;
    const targetLanguage = document.getElementById("language-select").value;
    const model = document.getElementById("model-select").value;

    const response = await fetch("/translate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: text, target_language: targetLanguage, model:model }),
    });

    const result = await response.json();
    document.getElementById("result-text").textContent = result.translated_text || result.error;
}
