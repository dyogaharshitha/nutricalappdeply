$(document).ready(function(){
$("#hdr").html("jk");
 const hdr= document.getElementById("hdr");
    // Add list to body (or anywhere else)
   // window.onload = function () {
        var navItems = [
        {'href': '{{ url_for('showhomepg') }}', 'text': 'Home'},
        {'href': 'http://bing.com', 'text': 'Bing'},
        {'href'': '{{ url_for('calnutri') }}', 'text'': 'calculate nutrition'}
    ];

    // A few variables for use later
    var navbr = document.createElement("NAV"); var btn= document.createElement("button");
     var navList = document.createElement("ul"); btn.innerHTML= "btn";
      var navItem;  var navLink;

        hdr.appendChild(navbr);
    navbr.appendChild(navList); navList.appendChild(btn);
    navbr.className = "navbar navbar-expand-lg bg-light";
    navList.className = "navbar-nav mr-auto mt-2"; navList.setAttribute("id", "nvlst");
     btn.className = "navbar-toggler"; //btn.setAttribute("data-toggle", "collapse"); btn.setAttribute("data-target","#nvlst"); //data-toggle= "collapse"; btn.data-target= "#nvlst";

    // Cycle over each nav item
    for (var i = 0; i < navItems.length; i++) {  //navItems.length
        // Create a fresh list item, and anchor
        navItem = document.createElement("li");
        navLink = document.createElement("a");

        // Set properties on anchor
        navLink.href =  navItems[i]['href'];
        navLink.innerHTML =   navItems[i]['text'];

        // Add anchor to list item, and list item to list
        navItem.appendChild(navLink); navItem.className = "nav-item"; navLink.className = "nav-link";
        navList.appendChild(navItem);
    }
 // Set first list item as current
  //  navList.children[0].className = "current";
  //  }

});



