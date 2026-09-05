async function askQuestion() {
    const question = document.getElementById("question").value;
    const answerBox = document.getElementById("answer");

    if (!question.trim()) {
        answerBox.innerText = "Please enter a question.";
        return;
    }

    answerBox.innerText = "Thinking...";

    try {
        const response = await fetch(
            "/api/text?question=" + encodeURIComponent(question),
            {
                method: "POST"
            }
        );

        const data = await response.json();

        if (!response.ok) {
            answerBox.innerText = "Error: " + JSON.stringify(data);
            return;
        }

        answerBox.innerText = data.answer;

    } catch (error) {
        answerBox.innerText = "Connection error: " + error.message;
        console.error(error);
    }
}