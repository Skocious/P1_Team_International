const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");
const id_name = loginForm.id_name.value;
const password = loginForm.password.value;
localURL = "http://192.168.1.130:5000/login"
// loginButton.addEventListener("click", (e) => {
// //     e.preventDefault(); // for testing - remove when ready to submit data upon click    
//     window.localStorage.setItem("id_name", loginForm.id_name.value);
//     window.localStorage.setItem("password", loginForm.password.value);
    
async function loginFunc(){
    loginButton.loginFunc.addEventListener("click", (e) => {
        e.preventDefault();
        window.localStorage.setItem("id_name", loginForm.id_name.value);
        window.localStorage.setItem("password", loginForm.password.value);
    loginInfoJSON = {
        "username": id_name,
        "password": password
    }
    let loginCredentials = {
        method:"POST",
        headers:{"Content-Type": "application/json"},
        body: JSON.stringify(loginInfoJSON)
    }
    fetch(localURL, loginCredentials)
        .then(response=> response.json)
        .then(data=> console.log(data));
    if(username === "id_name" && password ==="password") {
        
        window.location.href="employee_homepage.html"
        location.reload
    } else {
      loginErrorMsg.style.opacity =1;
      }
    }  ) }