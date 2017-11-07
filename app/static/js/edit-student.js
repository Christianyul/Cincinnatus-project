var reference_json = document.getElementsByTagName("h1")[0];
var input_name = document.getElementById("name"), input_last = document.getElementById("last_name"), 
input_email = document.getElementById("email"), input_birthdate = document.getElementById("birthdate"), 
input_inscription = document.getElementById("inscription_date"), input_ending = document.getElementById("ending_date")
input_retirement = document.getElementById("retirement_date"), input_cellphone = document.getElementById("phone_mobile")
input_phonehome = document.getElementById("phone_home"), input_identification = document.getElementById("id_document"),
input_address = document.getElementById("address");
console.log(input_name, input_last, input_email, input_retirement);
$.ajax({
  url: "http://localhost:5000/student/studentapi",
  contentType: document.body
}).done(function(data) {
  data.All_Data.forEach(function(element) {
    if (element.name == reference_json.innerHTML) {
      input_name.value = element.name, input_last.value = element.last_name, input_email.value = element.email,
      input_birthdate.value = element.birthdate, input_inscription.value = element.incription_date, input_ending.value = element.ending_date,
      input_retirement.value = element.retirement_date, input_cellphone.value = element.phone_mobile, input_phonehome.value = element.phone_home,
      input_identification.value = element.id_document, input_address.value = element.address;
    }
  }, this);
});