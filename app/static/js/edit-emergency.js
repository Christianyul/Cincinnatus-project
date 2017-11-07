var pageurl = location.href;
pageurl_id = pageurl.split("/")[3];
pageurl_id2 = pageurl.split("/")[5];
console.log(pageurl_id, pageurl_id2);
var h1text = document.getElementsByTagName('h1')[0], inputname = document.getElementById('name'),
inputlast = document.getElementById('last_name'), inputphone = document.getElementById('phone_home'),
inputmobile = document.getElementById('phone_mobile'), inputrelation = document.getElementById('relationship');
$.ajax({
    url: "http://localhost:5000/" + pageurl_id + "/emergency/emergencyapi",
    contentType: document.body
}).done(function(data){
    console.log(data);
    data.All_Data.forEach(function(element){
        if (element.Name_Emergency_Contact == h1text.innerText) {
            inputname.value = element.Name_Emergency_Contact;
            inputphone.value = element.Emergency_Phone_Home;
            inputmobile.value = element.Emergency_Phone_Mobile;
            inputrelation.value = element.Relationship_with_the_contact;
            inputlast.value = element.last_name;
            console.log('Done');
        }
    }, this);
})