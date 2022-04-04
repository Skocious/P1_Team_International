const id_name = document.getElementById("username-field");
const password = document.getElementById("password-field");

// 1	test1	test11

async function loginFunction() {

    console.log(id_name.value)
    console.log(password.value)
    let loginInfoJSON = {
        "id_name": id_name.value,
        "password": password.value
    }
    let loginCredentials = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(loginInfoJSON)
    }
    const httpResponse = await fetch("http://127.0.0.1:5000/login", loginCredentials)
    if (httpResponse.status == 200) { // or whatever code you are looking for
        const httpResponseBody = await httpResponse.json()
        window.localStorage.setItem('employee_id', httpResponseBody['employee_id'])
        alert('Wellcome' + " " + httpResponseBody["first_name"] + " " + httpResponseBody["last_name"])
        window.location.href = "employee_homepage.html"
            // alert(window.localStorage.getItem('employee_id'))
    } else {
        alert("Wrong Login Info Please, Try Again")
    }

}