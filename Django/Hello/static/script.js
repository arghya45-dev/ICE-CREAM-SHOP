document.addEventListener("DOMContentLoaded", function () {
    const snowflakeContainer = document.getElementById("snowflakes-container");
    let snowflakeCount = 0;
    const maxSnowflakes = 30; // Maximum number of snowflakes

    function createSnowflake() {
        if (snowflakeCount >= maxSnowflakes) return; // Stop when max is reached

        let snowflake = document.createElement("div");
        snowflake.className = "snowflake";
        snowflake.innerHTML = "❄";
        snowflake.style.left = Math.random() * 100 + "vw"; // Random horizontal position
        snowflake.style.animationDuration = (Math.random() * 5 + 5) + "s"; // Random fall speed
        snowflake.style.animationDelay = "0s"; // No delay for first snowflake

        snowflakeContainer.appendChild(snowflake);
        snowflakeCount++;
    }

    // Start with one snowflake, then add one every 500ms
    createSnowflake();
    setInterval(createSnowflake, 500); // Adds a snowflake every 500ms
});
