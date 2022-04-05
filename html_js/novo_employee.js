const reimbTableHead = document.getElementById("reimbHead");
const reimbTableBody = document.getElementById("tableBody");
employees_id = window.localStorage.getItem("id_name");

function currentEmpReqest(returnedInfo){  
    reimbTableBody.innerHTML = "";
    for(let obj in returnedInfo){
        //console.log(returnedInfo[obj])
        const newRow = document.createElement("tr");
        newRow.appendChild(newRow);
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
            tData.id = reqId
            reqId ++
        }

    }
}

async function requestEmployeeRequests(){
    
    let getURL = `http://127.0.0.1:5000/get_all_requests_by_employee_id`
    const response = await fetch(getURL, {method:"GET"})
    
    if (response.status === 200) {
        const returnedInfo = await response.json();
        console.log(returnedInfo);
        currentEmpReqst(returnedInfo);
    } else {
        alert(`Try again`);
    }
}


async function createReimbusementRequest(){
    
    let newRequestInfo = {
        "reimbursement_type": document.getElementById("category"),
        "balance": document.getElementById("amount"),
        "comment": document.getElementById("comment"),
        "status": "pending",
        //"employees_id": employee_id
    }

    let newRequest = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newRequestInfo)
    }

    const response = await fetch("http://127.0.0.1:5000/create_reimbursement_request", newRequest)
    if (response.status === 200) {
        const responseBody = await response.json()
        window.localStorage.setItem("reimbursement_type", "balance", "comment", responseBody[employees_id])
        alert("You have successfully created a reimbursement request!")
        //currentEmpReqst()
    }
}

async function cancelReimbusementRequest(){
 
    let cancelRequest = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(employees_id)
    }

    const cresponse = await fetch("http://127.0.0.1:5000/cancel_reimbursement_request", cancelRequest)
    if (cresponse.status === 200) {
        const cresponseBody = await cresponse.json()
        window.localStorage.removeItem("can i call the row here and delete all data?", cresponseBody[request_id])
        alert("You have successfully cancled a reimbursement request!")
        //currentEmpReqst()
    }
}

function clearStore_return_to_login(){
    window.localStorage.clear();
    window.location.href ="novo_edge_home.html";
}
