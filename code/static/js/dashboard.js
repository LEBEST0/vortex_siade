document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.getElementById("imageInput");
    const previewImage = document.getElementById("previewImage");
    const imageLabel = document.getElementById("imageLabel");
    const loadingText = document.getElementById("loadingText");
    const resultSection = document.getElementById("resultSection");
    const analysisResult = document.getElementById("analysisResult");
    const expertValidation = document.getElementById("expertValidation");
    const historyTable = document.getElementById("historyTable");
    const downloadPdfButton = document.getElementById("downloadPdf");

    // Gestion de l'affichage de l'image téléversée
    fileInput.addEventListener("change", function (event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            loadingText.style.display = "block"; // Affichage du texte de chargement

            reader.onload = function (e) {
                setTimeout(() => { // Simulation d'un délai
                    previewImage.src = e.target.result;
                    previewImage.style.display = "block";
                    imageLabel.style.display = "block";
                    loadingText.style.display = "none"; // Cacher le chargement
                }, 1000);
            };
            reader.readAsDataURL(file);
        }
    });

    // Gestion de la soumission du formulaire
    document.getElementById("uploadForm").addEventListener("submit", function (e) {
        e.preventDefault();

        // Récupération des valeurs des champs
        let nom = document.getElementById("nom").value.trim();
        let prenom = document.getElementById("prenom").value.trim();
        let datenaissance = document.getElementById("datenaissance").value;
        let telephone = document.getElementById("telephone").value.trim();
        let imageFile = fileInput.files[0];

        if (!nom || !prenom || !datenaissance || !telephone || !imageFile) {
            alert("Veuillez remplir tous les champs et téléverser une image.");
            return;
        }

        // Simulation du traitement
        resultSection.style.display = "block";
        analysisResult.innerText = "Analyse en cours...";

        setTimeout(() => {
            let scoreConfiance = Math.random(); // Générer un score aléatoire
            let resultat = scoreConfiance > 0.6 ? 
                "Présence détectée de parasites du paludisme." : 
                "Aucune trace détectée.";

            analysisResult.innerText = resultat;

            // Affichage du bouton de vérification si le score est faible
            if (scoreConfiance < 0.5) {
                expertValidation.style.display = "block";
            } else {
                expertValidation.style.display = "none";
            }

            // Ajout de l'analyse à l'historique
            let row = historyTable.insertRow();
            row.innerHTML = `
                <td>${nom}</td>
                <td>${prenom}</td>
                <td>${new Date().toLocaleDateString()}</td>
                <td><button class='btn btn-info voir-resultat'>Voir</button></td>
            `;

            // Gestion du bouton "Voir" pour afficher le résultat correspondant
            row.querySelector(".voir-resultat").addEventListener("click", function () {
                alert(`Résultat de l'analyse pour ${nom} ${prenom} :\n${resultat}`);
            });

        }, 2000);
    });

    // Téléchargement du rapport PDF (simulation)
    downloadPdfButton.addEventListener("click", function () {
        alert("Téléchargement du rapport PDF...");
    });
});
