document.addEventListener("DOMContentLoaded", function () {

    // =========================
    // MPG PREDICTION
    // =========================
    const form = document.getElementById("predict-form");
    const resultBox = document.getElementById("result");
    const mpgValue = document.getElementById("predictedMPG");
    const efficiencyText = document.getElementById("efficiencyText");
    const featuresGrid = document.getElementById("featuresGrid");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        let formData = new FormData(form);

        let response = await fetch("https://car-fuel-efficiency-predictor.onrender.com/predict", {
            method: "POST",
            body: formData
        });


        let res = await response.json();

        if (res.success) {
            resultBox.style.display = "block";
            mpgValue.textContent = res.prediction;

            featuresGrid.innerHTML = `
                <p><strong>Cylinders:</strong> ${formData.get("cylinders")}</p>
                <p><strong>Displacement:</strong> ${formData.get("displacement")}</p>
                <p><strong>Horsepower:</strong> ${formData.get("horsepower")}</p>
                <p><strong>Weight:</strong> ${formData.get("weight")}</p>
                <p><strong>Model Year:</strong> ${formData.get("model_year")}</p>
            `;
        }
    });

    // =========================
    // FUEL COST CALCULATOR
    // =========================
    const calcBtn = document.getElementById("calcFuel");
    const fuelResult = document.getElementById("fuelResult");
    const fuelText = document.getElementById("fuelCostText");

    calcBtn.addEventListener("click", function () {
        let dist = parseFloat(document.getElementById("distance").value);
        let price = parseFloat(document.getElementById("fuelPrice").value);
        let mpg = parseFloat(document.getElementById("predictedMPG").textContent);

        if (isNaN(mpg) || mpg <= 0) {
            alert("Please calculate MPG first!");
            return;
        }

        let kmPerLiter = mpg * 0.4251; 
        let litersUsed = dist / kmPerLiter;
        let cost = litersUsed * price;

        fuelResult.style.display = "block";
        fuelText.textContent = `Estimated yearly cost: Rs. ${cost.toFixed(0)}`;
    });

});
