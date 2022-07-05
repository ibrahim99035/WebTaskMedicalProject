//spans
let heartSpan = document.querySelector('#heart');
let diapSpan  = document.querySelector('#diap');
let surgSpan  = document.querySelector('#surg');
let CoronaSpan = document.querySelector('#coronaSpan');
let KidenySpan = document.querySelector('#KidneySpan')
let coronaInOutSpan = document.querySelector('#CoronaInOut')
let BrainTumourSpan = document.querySelector('#brainTumourSpan')

//divs
let heartDiv  = document.querySelector('#heartPred');
let diapDiv  = document.querySelector('#diapetes');
let surgDiv  = document.querySelector('#surgical');
let defult = document.querySelector('#default');
let coronaDiv = document.querySelector('#corona');
let kidneyDiv = document.querySelector('#KidneyDiv')
let coronaInOutDiv = document.querySelector('#coronaInOutDiv')
let BrainTumourDiv = document.querySelector('#braintumourDiv')



//events
heartSpan.addEventListener('click', () => {
    heartDiv.style.display = "block";
    diapDiv.style.display = "none";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    coronaDiv.style.display = "none";
    treatment.style.display = "none";
    kidneyDiv.style.display = "none";
    BrainTumourDiv.style.display = "none";
    coronaInOutDiv.style.display = "none";
});

diapSpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "block";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    coronaDiv.style.display = "none";
    treatment.style.display = "none";
    kidneyDiv.style.display = "none";
    BrainTumourDiv.style.display = "none";
    coronaInOutDiv.style.display = "none";
});


surgSpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "none";
    surgDiv.style.display = "block";
    defult.style.display = "none";
    coronaDiv.style.display = "none";
    treatment.style.display = "none";
    kidneyDiv.style.display = "none";
    BrainTumourDiv.style.display = "none";
    coronaInOutDiv.style.display = "none";
});


CoronaSpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "none";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    treatment.style.display = "none";
    coronaInOutDiv.style.display = "none";
    coronaDiv.style.display = "block";
    kidneyDiv.style.display = "none";
    BrainTumourDiv.style.display = "none";
});

KidenySpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "none";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    treatment.style.display = "none";
    coronaDiv.style.display = "none";
    coronaInOutDiv.style.display = "none";
    kidneyDiv.style.display = "block";
    BrainTumourDiv.style.display = "none";
});

coronaInOutSpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "none";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    treatment.style.display = "none";
    coronaDiv.style.display = "none";
    kidneyDiv.style.display = "none";
    coronaInOutDiv.style.display = "block";
    BrainTumourDiv.style.display = "none";
})


BrainTumourSpan.addEventListener('click', () => {
    heartDiv.style.display = "none";
    diapDiv.style.display = "none";
    surgDiv.style.display = "none";
    defult.style.display = "none";
    coronaDiv.style.display = "none";
    treatment.style.display = "none";
    kidneyDiv.style.display = "none";
    coronaInOutDiv.style.display = "none";
    BrainTumourDiv.style.display = "block";
});



//adding patients
//spans
let patinetSpan1 = document.querySelector('#patinetSpan1');
let patinetSpan2 = document.querySelector('#patinetSpan2');
let patinetSpan3 = document.querySelector('#patinetSpan3');
let patinetSpan4 = document.querySelector('#patinetSpan4');
let patinetSpan5 = document.querySelector('#patinetSpan5');
//forms
let patientForm5 = document.querySelector('#patientForm5');
let patientForm4 = document.querySelector('#patientForm4');
let patientForm3 = document.querySelector('#patientForm3');
let patientForm2 = document.querySelector('#patientForm2');
let patientForm1 = document.querySelector('#patientForm1');
//patients forms events
patinetSpan1.addEventListener('click', () => {
    patientForm1.style.display = "block";
});
patinetSpan2.addEventListener('click', () => {
    patientForm2.style.display = "block";
});
patinetSpan3.addEventListener('click', () => {
    patientForm3.style.display = "block";
});
patinetSpan4.addEventListener('click', () => {
    patientForm4.style.display = "block";
});
patinetSpan5.addEventListener('click', () => {
    patientForm5.style.display = "block";
});
