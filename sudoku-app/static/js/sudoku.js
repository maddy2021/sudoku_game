const BACKTRACK_URL = "/sudoku/solve/backtracking";
const NORVING_URL = "/sudoku/solve/norving";
const VALIDATE_URL = "/sudoku/validate";
const GENERATE_URL = "/sudoku/random/generate"

const VALIDATE_BUTTON = document.getElementById('validate_btn');
const NORVING_BUTTON = document.getElementById('norving_btn');
const BACKTRACT_BTN = document.getElementById('solve_backtrack_btn');
const GENERATE_BUTTON = document.getElementById('generate_btn');

VALIDATE_BUTTON.addEventListener('click', ()=>{   
    let sudokuString = document.getElementById('sudoku_string').value;
    if(validateString(sudokuString)){
    $.ajax({
        contentType: 'application/json',
        data:JSON.stringify({
            "input_str":sudokuString
        }),
        url: VALIDATE_URL,
        type: 'POST',
    success: function(response) {
        if(response["valid"]=="true"){
            populateInTable(sudokuString,"");
    }else{
        alert("provide valid input");
    }
    },
    error: function(error) {
        console.log(error);
    }
});              
}
});


NORVING_BUTTON.addEventListener('click', ()=>{   
    question_str = makeString()
    clearData(question_str,"solve-")
    document.getElementById("execution_time").textContent = 0 ;
    showLoader();
    $.ajax({
        contentType: 'application/json',
        data:JSON.stringify({
            "input_str":makeString()
        }),
        url: NORVING_URL,
        type: 'POST',
        success: function(response) {
                populateInTable(response["solution_String"],"solve-");
                document.getElementById("execution_time").textContent =response["execution_time"] ;
                hideLoader();
    },
    error: function(error) {
        console.log(error);
    }
});       
});

BACKTRACT_BTN.addEventListener('click', ()=>{   
    //let sudokuString = document.getElementById('sudoku_string').value;
    question_str = makeString()
    clearData(question_str,"solve-")
    document.getElementById("execution_time").textContent = 0 ;
    showLoader();
    $.ajax({
        contentType: 'application/json',
        data:JSON.stringify({
            "input_str":makeString()
        }),
        url: BACKTRACK_URL,
        type: 'POST',
        success: function(response) {
            if(response["valid"]=="true"){
                populateInTable(response["solution_String"],"solve-");
                document.getElementById("execution_time").textContent =response["execution_time"] ;
                document.body.className="";
                hideLoader();
        }else{
            hideLoader();
        alert("provide valid input");
        }
    },
    error: function(error) {
        hideLoader();
        console.log(error);
    }
});       
});




GENERATE_BUTTON.addEventListener('click', ()=>{   
    //let sudokuString = document.getElementById('sudoku_string').value;
    // clearData(question_str,"")
    $.ajax({
    contentType: 'application/json',
    url: GENERATE_URL,
    type: 'GET',
    success: function(response) {
        if(response["sudoku_str"]){
        console.log(response)
            populateInTable(response["sudoku_str"],"");
        }else{
        alert("provide valid input");
        }
    },
    error: function(error) {
        console.log(error);
    }
});       
});




const validateString = (str) => {
    if(str.length==0){
        alert("please provide input");
        return false;
    }
    else if(str.length>0 && str.length<81 || str.length>81){
        alert("Input must have 81 character");
        return false;
    }
    if(str.match("^[0-9\.]+$")==null){
        // console.log("in pattern")
        alert("Input must have 81 character");
        return false;
    }
    else if(str.length==81){
        return true;
    }
}


const populateInTable=(str,id)=>{
    i=0;
    for(i=0;i<str.length;i++){
        document.getElementById(id+"cell-"+i).value = str[i];
    };
}

const makeString=()=>{
    //console.log(document.getElementById('grid'));
    str = ""
    i=0;
    for(i=0;i<81;i++){
    if(document.getElementById("cell-"+i).value==""){
        str+=".";    
    }
    str+=document.getElementById("cell-"+i).value;
    }
    console.log(str)
    return str;
}


const clearData=(str,id)=>{
    i=0;
    for(i=0;i<str.length;i++){
    document.getElementById(id+"cell-"+i).value = "";
    };
}


const showLoader=()=>{
    document.getElementById("loader").style.display="block";
    document.getElementById("solve_backtrack_btn").disabled= true;
    document.getElementById("norving_btn").disabled = true;
    document.getElementById("generate_btn").disabled = true;
}


const hideLoader=()=>{
    document.getElementById("loader").style.display="none";
    document.getElementById("solve_backtrack_btn").disabled= false;
    document.getElementById("norving_btn").disabled = false;
    document.getElementById("generate_btn").disabled = false;
}