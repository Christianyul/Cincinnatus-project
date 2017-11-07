var pageurl = location.href;
pageurl_id = pageurl.split("/")[3];
console.log(pageurl_id);
var h1text = document.getElementsByTagName('h1')[0], inputalergies = document.getElementById('alergies'),
inputspecial = document.getElementById('special_condition'), inputars = document.getElementById('ars'),
inputpolicy = document.getElementById('policy_number'), inputafiliation = document.getElementById('afiliation_type');
$.ajax({
    url: "http://localhost:5000/" + pageurl_id + "/medical/medicalapi",
    contentType: document.body
}).done(function(data){
    console.log(data);
    data.All_Data.forEach(function(element){
        if (element.id == pageurl_id) {
            inputalergies.value = element.alergies_of_the_student;
            inputspecial.value = element.Special_Condition;
            inputars.value = element.Ars;
            inputpolicy.value = element.policy_number;
            inputafiliation.value = element.Afliation_type;
            console.log('Done');
        }
    }, this);
})