// const reimb_table = document.getElementById("reimbursement-status");
// const reimbt_employeeid = document.getElementById("employeeidt");



localURL = "https://localhost:5000/login_employee"
// alert(`your id is ${window.localStorage.getItem("username")}`);


employees_id = window.localStorage.getItem("username");
employees_password = window.localStorage.getItem("password");
async function getPassword(){
    let response = fetch(localURL + employees_password);
}





// async function makeReimbRequest(){
//     const response = await fetch(localURL + employees_id, {method:"Get"})
//     if (response.status === 200) {
//         const einfo = await response.json();
//         add_to_table(einfo)
//     } else {
//         alert(`Bad Info`);
//     }
// }

// function add_to_table() {
//     for 

// }







// const reimb_row = document.getElementById("body")
// const newTableRow = document.createElement("tr")

// reimb_table.appendChild(newTableRow);

// newTableRow.innerHTML = `<`




function clearStore_return_to_login(){
    window.localStorage.clear();
    window.location.href ="novo_edge_home.html";
}
