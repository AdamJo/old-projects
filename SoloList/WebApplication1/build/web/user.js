var numlists = 0;
$( document ).ready(function() {
    $.ajax({
        type: "GET",
        url: "/resources/playlist/playlists"+location.search
    }).done(function( msg ) {
        $("#playlist").append("<div id=\"playlistgrid\" class=\"ui-grid-c\"></div>");
        $.each( msg, function( key, value ) {
            $("#playlistgrid").append("<div id=\"playlistgrid"+key+"\"/>");
        });
        $.each( msg, function( key, value ) {
            $("#playlistgrid"+key).replaceWith("<div class=\""+key+" ui-block-a\" style=\"height:45px;width:25%;\"></div>"
                +"<div class=\""+key+" ui-block-b\" style=\"height:45px;width:30%;\"><div class=\"ui-bar ui-bar-e\"><a class=\"newlist"+key+"\" data-ajax=\"false\" href=\"/playlist.jsp?p="+value[0]+"\">"+value[1]+"</a></div></div>"
                +"<div class=\""+key+" ui-block-c\" style=\"height:45px;width:10%;\"><a href=\"#\" class=\"editbtn editbtn"+key+" ui-btn ui-shadow ui-corner-all ui-icon-edit ui-btn-icon-notext\"><div class=\"ui-bar ui-bar-e\">Edit</div></a></div>"
                +"<div class=\""+key+" ui-block-d\" style=\"height:45px;width:10%;\"><a href=\"#\" class=\"removebtn removebtn"+key+" ui-btn ui-shadow ui-corner-all ui-icon-delete ui-btn-icon-notext\"><div class=\"ui-bar ui-bar-e\">Delete</div></a></div>"
            );
            $(".editbtn"+key).click(function() {
                $(".newlist"+key).replaceWith("<input class=\"newlistedit"+key+"\" type=\"text\" value=\""+$(".newlist"+key).html()+"\"/>");
                $(".newlistedit"+key).blur(function() {
                    $.ajax({
                        type: "GET",
                        url: "/resources/playlist/rename?p="+value[0]+"&t="+$(".newlistedit"+key).val()
                    }).done(function( msg ) {
                        $(".newlistedit"+key).replaceWith("<a class=\"newlist"+key+"\" data-ajax=\"false\" href=\"/playlist.jsp?p="+value[0]+"\">"+$(".newlistedit"+key).val()+"</a>");
                    });
                });
                 $(".newlistedit"+key).keyup(function(e){
                    if(e.keyCode == 13)
                    {
                        $.ajax({
                            type: "GET",
                            url: "/resources/playlist/rename?p="+value[0]+"&t="+$(".newlistedit"+key).val()
                        }).done(function( msg ) {
                            $(".newlistedit"+key).replaceWith("<a class=\"newlist"+key+"\" data-ajax=\"false\" href=\"/playlist.jsp?p="+value[0]+"\">"+$(".newlistedit"+key).val()+"</a>");
                        });
                    }
                 });
            });
            $(".removebtn"+key).click(function() {
                 $.ajax({
                    type: "GET",
                    url: "/resources/playlist/removelist?p="+value[0]
                 }).done(function( msg ) {
                    $("."+key).remove();
                });

            });
            numlists++;
        });
        
        $("#addplaylistbtn").click(function() {
            $.ajax({
                type: "GET",
                url: "/resources/playlist/new"+location.search
            }).done(function( msg ) {
                key = numlists.length - 1;
                $("#playlistgrid").append("<div class=\"ui-block-a\" style=\"height:45px;width:25%;\"></div>"
                    +"<div class=\"ui-block-b\" style=\"height:45px;width:30%;\"><div class=\"ui-bar ui-bar-e\"><a class=\"newlist"+key+"\" data-ajax=\"false\" href=\"/playlist.jsp?p="+msg+"\">New Playlist</a></div></div>"
                    +"<div class=\"ui-block-c\" style=\"height:45px;width:10%;\"><a href=\"#\" class=\"editbtn editbtn"+key+" ui-btn ui-shadow ui-corner-all ui-icon-edit ui-btn-icon-notext\"><div class=\"ui-bar ui-bar-e\">Edit</div></a></div>"
                    +"<div class=\"ui-block-d\" style=\"height:45px;width:10%;\"><a href=\"#\" class=\"removebtn removebtn"+key+" ui-btn ui-shadow ui-corner-all ui-icon-delete ui-btn-icon-notext\"><div class=\"ui-bar ui-bar-e\">Delete</div></a></div>"
                );
                $(".editbtn"+key).click(function() {
                    $(".newlist"+key).replaceWith("<input class=\"newlistedit"+key+"\" type=\"text\" value=\""+$(".newlist"+key).html()+"\"/>");
                    $(".newlistedit"+key).blur(function() {
                        $.ajax({
                            type: "GET",
                            url: "/resources/playlist/rename?p="+value[0]+"&t="+$(".newlistedit"+key).val()
                        }).done(function( msg ) {
                            $(".newlistedit"+key).replaceWith("<a class=\"newlist"+key+"\" data-ajax=\"false\" href=\"/playlist.jsp?p="+value[0]+"\">"+$(".newlistedit"+key).val()+"</a>");
                        });
                    });
                     $(".newlistedit"+key).keyup(function(e){
                        if(e.keyCode == 13)
                        {
                            $.ajax({
                                type: "GET",
                                url: "/resources/playlist/rename?p="+value[0]+"&t="+$(".newlistedit"+key).val()
                            }).done(function( msg ) {
                                $(".newlistedit"+key).replaceWith("<a class=\"newlist"+key+"\" data-ajax=\"false\" href=\"/playlist.jsp?p="+value[0]+"\">"+$(".newlistedit"+key).val()+"</a>");
                            });
                        }
                     });
                });
                $(".removebtn"+key).click(function() {
                     $.ajax({
                        type: "GET",
                        url: "/resources/playlist/removelist?p="+value[0]
                     }).done(function( msg ) {
                        $("."+key).remove();
                    });

                });
                numlists++;
            });
        });
    });
});
