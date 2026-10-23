console.log("Start of Website")



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

