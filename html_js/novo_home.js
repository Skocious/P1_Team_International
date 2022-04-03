const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");
const username = loginForm.username.value;
const password = loginForm.password.value;
localURL = "https://localhost:5000/login_employee"
// loginButton.addEventListener("click", (e) => {
// //     e.preventDefault(); // for testing - remove when ready to submit data upon click    
//     window.localStorage.setItem("username", loginForm.username.value);
//     window.localStorage.setItem("password", loginForm.password.value);
    
async function loginFunc(){
    loginButton.loginFunc.addEventListener("click", (e) => {
        e.preventDefault();
        window.localStorage.setItem("username", loginForm.username.value);
        window.localStorage.setItem("password", loginForm.password.value);
    loginInfoJSON = {
        "username": username,
        "password": password
    }
    let loginCredentials = {
        method:"POST",
        headers:{"Content-Type": "application/json"},
        body: JSON.stringify(loginInfoJSON)
    }
    if(username === "username" && password ==="password") {
        fetch(localURL, loginCredentials)
        .then(response=> response.json)
        .then(data=> console.log(data));
        window.location.href="employee_homepage.html"
        location.reload
    } else {
      loginErrorMsg.style.opacity =1;
    }
