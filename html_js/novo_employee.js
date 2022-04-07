const reimbTableHead = document.getElementById("reimbHead");
const reimbTableBody = document.getElementById("tableBody");
const employee_id = window.localStorage.getItem("employee_id");
const reimbursementType = document.getElementById("category")
const balance = document.getElementById("amount")
const comment = document.getElementById("comment")


function currentEmpReqest(returnedInfo) {
    reimbTableBody.innerHTML = "";
    let requestId = 1
    for (let obj in returnedInfo) {
        //console.log(returnedInfo[obj])
        const newRow = document.createElement("tr");
        reimbTableBody.appendChild(newRow);
        const balance = returnedInfo[obj].balance;
        const comment = returnedInfo[obj].comment;
        //const employee_id = returnedInfo[obj].employee_id;
        const reimbursement_type = returnedInfo[obj].reimbursement_type;
        const request_id = returnedInfo[obj].request_id;
        const status = returnedInfo[obj].status;

        returnedInfoList = [balance, comment, reimbursement_type, request_id, status];
        for (let elements of returnedInfoList) {
            const tData = document.createElement("td");
            tData.textContent = elements
            newRow.appendChild(tData)
            tData.id = requestId
            requestId++
        }

    }
}

async function requestEmployeeRequests() {

    let getURL = "http://127.0.0.1:5000/get_all_requests_by_employee_id/"

    let response = await fetch(getURL + employee_id, { method: "GET" })

    if (response.status === 200) {
        let returnedInfo = await response.json();
       // console.log(returnedInfo);
        currentEmpReqest(returnedInfo);
 }  else if (response.status === 400) {
        let responseBody = await response.json()
        alert(responseBody.message);
    }
}


async function createReimbursementRequest() {

    let newRequestInfo = {
        "reimbursement_type": reimbursementType.value,
        "balance": balance.value,
        "comment": comment.value,
        "employee_id": employee_id
    }
    console.log(newRequestInfo)
    let newRequest = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newRequestInfo)
    }
    let response = await fetch("http://127.0.0.1:5000/create_reimbursement_request", newRequest)
    if (response.status === 200) {
        alert("You have successfully created a reimbursement request!")
        totalBalances();
        requestEmployeeRequests();
  } else if (response.status === 400) {
        let responseBody = await response.json()
        alert(responseBody.message);   
    }
    
}

async function cancelReimbursementRequest() {

    let requestCancelID = document.getElementById("cancelReq")
    let cresponse = await fetch("http://127.0.0.1:5000/cancel_reimbursement_request/" + requestCancelID.value)
    if (cresponse.status === 200) {
        alert("You have successfully canceled a reimbursement request!")
        totalBalances();
        requestEmployeeRequests();
  } else if (cresponse.status === 400) {
        let responseBody = await cresponse.json()
        alert(responseBody.message);  
    }
}

async function totalBalances() {
    let totalBalanceOwed = document.getElementById("openBalance")
    let bresponse = await fetch("http://127.0.0.1:5000/get_sum_requests_amount_by_employee_id/" + employee_id)
    if (bresponse.status === 200) {
       // console.log(bresponse)
       const value = await bresponse.json()
       // console.log(value)
       totalBalanceOwed.textContent = value
  } else if (bresponse.status === 400) {
        let responseBody = await bresponse.json()
        alert(responseBody.message);
}
    
}

function clearStore_return_to_login() {
    window.localStorage.clear();
    window.location.href = "novo_edge_home.html";
}
totalBalances();
requestEmployeeRequests();

//over 100 char
// I took a trip to Denver and had an omlette with ham, cheddar cheese, monteray jack cheese, onoins and peppers. 

// under 100 char
// I walked from my ashram at Sabermanti 240 miles to the Dandi on the Arabian Sea to buy salt.