// console.log("Start of Website")



const login = document.getElementById("login");
// const loginClose = document.getElementById("loginCross");
const loginOpen = document.getElementById("loginStart");
const adminOpen = document.getElementById("adminPanelOpen");
const adminClose = document.getElementById("adminCross");

// loginClose.addEventListener('click', function() {
//     login.style.display = 'none'; 
// });

loginOpen.addEventListener('click', function() {
    login.style.display = 'block'; 
    loginStart.style.display = 'none';
});

adminOpen.addEventListener('click', function() {
    adminPanel.style.display = 'block'; 
    adminCross.style.display = 'block';
    loginStart.style.display = 'none';
    login.style.display = 'none';
});

adminClose.addEventListener('click', function() {
    adminPanel.style.display = 'none'; 
    adminCross.style.display = 'blnoneock';
    loginStart.style.display = 'block';
});

let donneesRenvoyees = 0;

        const affichage = document.querySelector('#valeur-variable');

        
        function mettreAJour() {
            
            affichage.textContent = donneesRenvoyees; 
        }

        
        setInterval(mettreAJour, 1000);

const formulaire = document.getElementById('formulaireLogin');

  formulaire.addEventListener('submit', async function(event) {
    event.preventDefault();

    
    const formData = new FormData(formulaire);

    try {
      const reponse = await fetch('https://tirageausortnoel.onrender.com/login', {
        method: 'POST',
        body: formData 
      });

      
      const donneesRenvoyees = await reponse.json();

      
      console.log("Données reçues du serveur :", donneesRenvoyees);

      
      document.getElementById('reponseServeur').textContent = `Serveur dit : ${JSON.stringify(donneesRenvoyees)}`;

    } catch (erreur) {
      console.error("Erreur lors de la communication avec le serveur :", erreur);
      document.getElementById('reponseServeur').textContent = "Impossible de joindre le serveur.";
    }
  });

