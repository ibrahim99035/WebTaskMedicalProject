//spans
let heartSpan = document.querySelector('#heart');
let diapSpan  = document.querySelector('#diap');
let surgSpan  = document.querySelector('#surg');
let patientStaySpan  = document.querySelector('#stay');
let CoronaSpan = document.querySelector('#coronaSpan');
let KidenySpan = document.querySelector('#KidneySpan')


//divs
let heartDiv  = document.querySelector('#heartPred');
let diapDiv  = document.querySelector('#diapetes');
let surgDiv  = document.querySelector('#surgical');
let defult = document.querySelector('#default');
let treatment = document.querySelector('#treatment');
let coronaDiv = document.querySelector('#corona');
let kidneyDiv = document.querySelector('#KidneyDiv')



//events
heartSpan.addEventListener('click', () => {
    heartDiv.style.display = "block";
    diapDiv.style.display = "none";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    coronaDiv.style.display = "none";
    treatment.style.display = "none";
    kidneyDiv.style.display = "none";
});

diapSpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "block";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    coronaDiv.style.display = "none";
    treatment.style.display = "none";
    kidneyDiv.style.display = "none";
});


surgSpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "none";
    surgDiv.style.display = "block";
    defult.style.display = "none";
    coronaDiv.style.display = "none";
    treatment.style.display = "none";
    kidneyDiv.style.display = "none";
});

patientStaySpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "none";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    coronaDiv.style.display = "none";
    treatment.style.display = "block";
    kidneyDiv.style.display = "none";
});

CoronaSpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "none";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    treatment.style.display = "none";
    coronaDiv.style.display = "block";
    kidneyDiv.style.display = "none";
});

KidenySpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "none";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    treatment.style.display = "none";
    coronaDiv.style.display = "none";
    kidneyDiv.style.display = "block";
});
