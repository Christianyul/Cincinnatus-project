var inputname = document.getElementById("name"), inputlesson = document.getElementById("lesson"), 
inputlink = document.getElementById("link"), h1element = document.getElementsByTagName('h1')[0];
$.ajax({
    url: "http://localhost:5000/course/courseapi",
    contentType: document.body
}).done(function(data){
    console.log(data);
    data.Allcoursesdata.forEach(function(element){
        if(element.name == h1element.innerText){
            inputname.value = element.name;
            inputlink.value = element.link;
            inputlesson.value = element.lesson;
            console.log("Done");
        }
    }, this);
});