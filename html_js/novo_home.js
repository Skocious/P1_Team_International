const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault(); // for testing - remove when ready to submit data upon click
    const username = loginForm.username.value;
    const password = loginForm.password.value;
    window.localStorage.setItem("username", loginForm.username.value);
    window.localStorage.setItem("password", loginForm.password.value);
    

    if (username === "username" && password === "password") { //redirect to check db
        
        alert("You have successfully logged in."); // Here we will redirect to the employee home page
        window.location.href="employee_homepage.html";
        //location.reload();
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})

// defer is used on the script to make sure the JS runs after the html is fully loaded

// sql query example SELECT log_password FROM log_user WHERE log_username = %s (the username givin)

// select a field of the loginForm form as formElement.nameOfField, where formElement is your HTML<form> andnameOfField is the 
// value given to the name attribute of the <input> element you’re looking for. To get the value of the selected field, 
// just add .value. For example, if the user typed “user01” in the username field, then we’ll get that value with 
// loginForm.username.value