var h1tag = document.getElementsByTagName("h1")[0].innerText;
var inputname = document.getElementById("name"), inputusername = document.getElementById("user_name"), 
inputemail = document.getElementById("email");
$.ajax({
    url: "http://localhost:5000/user/usersapi",
    contentType: document.body, 
}).done(function(data){
    console.log(data);
    data.All_Data.forEach(function(element){
      if(element.UserName == h1tag){
          inputname.value = element.Name;
          inputemail.value = element.Email;
          inputusername.value = element.UserName;
      }
    }, this);
});