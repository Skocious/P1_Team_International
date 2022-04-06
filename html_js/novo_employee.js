const reimbTableHead = document.getElementById("reimbHead");
const reimbTableBody = document.getElementById("tableBody");
employees_id = window.localStorage.getItem("id_name");
const reimbursement_type = document.getElementById("category")

function currentEmpReqest(returnedInfo){  
    reimbTableBody.innerHTML = "";
    let requestId = 1
    for(let obj in returnedInfo){
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
            requestId ++
        }

    }
}


// function sumTransaction()
// {
//     var td = document.querySelectorAll('#table_trans > tbody > tr > td:last-child');
//     var total = 0;

//     for (var i = 0; i < td.length; i++)
//     {
//         total += parseInt(td[i].innerText);
//     }

//     document.getElementById('area_total').innerText = total;
// }

async function requestEmployeeRequests(){
    
    let getURL = `http://127.0.0.1:5000/get_all_requests_by_employee_id`
    const response = await fetch(getURL, {method:"GET"})
    
    if (response.status === 200) {
        const returnedInfo = await response.json();
        console.log(returnedInfo);
        currentEmpReqest(returnedInfo);
    } else {
        alert(`Try again`);
    }
}

//console.log(document.getElementById("amount"))
async function createReimbursementRequest(){
    
    let newRequestInfo = {
        
        "reimbursement_type": reimbursement_type.value,
        "balance": document.getElementById("amount"),
        "comment": document.getElementById("comment"),
        "status": "pending",
        "employees_id": window.localStorage.getItem("employee_id")
        
        
    }

    let newRequest = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newRequestInfo)
    }

    const response = await fetch("http://127.0.0.1:5000/create_reimbursement_request", newRequest.value)
    if (response.status === 200) {
        const responseBody = await response.json()
        //window.localStorage.setItem("reimbursement_type", "balance", "comment", responseBody[employees_id])
        alert("You have successfully created a reimbursement request!")
        requestEmployeeRequests()
    }
}

async function cancelReimbursementRequest(){
 
    let requestCancelID = document.getElementById("cancelReq")
    //console.log(requestCancelID.value)
    // let cancelRequest = {
    //     method: "GET",
    //     headers: { "Content-Type": "application/json" },
    //     body: JSON.stringify(employees_id),
    //     //mode: "cors"
    // }

    const cresponse = await fetch("http://127.0.0.1:5000/cancel_reimbursement_request/"+ requestCancelID.value)
    if (cresponse.status === 200) {
        const cresponseBody = await cresponse.json()
        
        alert("You have successfully canceled a reimbursement request!")
        requestEmployeeRequests()
    }
}

function clearStore_return_to_login(){
    window.localStorage.clear();
    window.location.href ="novo_edge_home.html";
}

requestEmployeeRequests()