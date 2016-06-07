
            function timeconvert (t) {
                var sec_num = parseInt(t, 10);
                var minutes = Math.floor(sec_num / 60);
                var seconds = sec_num - (minutes * 60);

                if (seconds < 10) {seconds = "0"+seconds;}
                var time    = +minutes+':'+seconds;
                return time;
            }

            var playlist;
            var noplaylist = [];
            function showplaylist (table) {
                $(table).append("<div id=\"playlistgrid\" class=\"ui-grid-c\"></div>");
                $.each( playlist, function( key, value ) {
                    $("#playlistgrid").append("<div id=\"playlistgrid"+key+"\"/>");
                });
                 $.each( playlist, function( key, value ) {
                         $.ajax({
                            type: "GET",
                            url: "http://gdata.youtube.com/feeds/api/videos/"+value+"?v=2&alt=jsonc"
                        }).done(function( msg ) {
                             $("#playlistgrid"+key).replaceWith("<a class=\"newsong"+key+"\" href=\"#\"><div class=\"ui-block-a\" style=\"height:45px;width:15%;\"><div class=\"ui-bar ui-bar-e\"><img style=\"height:40px\" src='"+msg.data.thumbnail.sqDefault+"'/></div></div>"
					+"<div class=\"ui-block-b\" style=\"height:45px;width:63%;\"><div class=\"ui-bar ui-bar-e\">"+msg.data.title+"</div></div>"
					+"<div class=\"ui-block-c\" style=\"height:45px;width:10%;\"><div class=\"ui-bar ui-bar-e\">"+timeconvert(msg.data.duration)+"</div></div></a>"
                                        +"<div class=\"ui-block-d\" style=\"height:45px;width:10%;\"><a href=\"#\" class=\"removebtn removebtn"+key+" ui-btn ui-shadow ui-corner-all ui-icon-delete ui-btn-icon-notext\"><div class=\"ui-bar ui-bar-e\">Delete</div></a></div>");
                            $(".newsong"+key).click(function() {
                                    player.loadVideoById(playlist[key]);
                                     activesongnum = key;
                            });
                           $(".removebtn"+key).click(function() {
                               var orderid = key+1
                               console.log("o"+key);
                                $.ajax({
                                    type: "GET",
                                    url: "/resources/playlist/remove"+location.search+"&o="+orderid
                                }).done(function( msg ) {
                                    noplaylist.push(key);
                                    $(".newsong"+key).remove();
                                    $(".removebtn"+key).remove();
                                    if(activesongnum == key) {
                                        if(activesongnum == key) {
                                            activesongnum++;
                                            while(noplaylist.indexOf(activesongnum) != -1) {
                                                if(playlist.length > activesongnum ) {
                                                    activesongnum++;
                                                }
                                            }
                                            if(playlist.length > activesongnum ) {
                                                player.loadVideoById(playlist[activesongnum])
                                            }
                                        }
                                    }
                                });
                            });
                        });
                    });
            }
            $( document ).ready(function() {
                $("#searchtext").keyup(function(e){                  
                    if(e.keyCode == 13){
                        $("#searchlist").html("");
                         $.ajax({
                            type: "GET",
                            url: "/resources/youtube/search?keyword="+$("#searchtext").val()
                        }).done(function( msg ) {
                            $("#searchlist").append("<div id=\"searchlistgrid\" class=\"ui-grid-c\"></div>");
                            $.each( msg, function( key, o ) {
                                 $.ajax({
                                type: "GET",
                                url: "http://gdata.youtube.com/feeds/api/videos/"+o.id.videoId+"?v=2&alt=jsonc"
                            }).done(function( msg ) {
                               $newsearchsong = "<a class=\"newaddsong"+key+"\" href=\"#\"><div class=\"ui-block-a\" style=\"height:45px;width:15%;\"><div class=\"ui-bar ui-bar-e\"><img style=\"height:40px\" src='"+msg.data.thumbnail.sqDefault+"'/></div></div>"
					+"<div class=\"ui-block-b\" style=\"height:45px;width:63%;\"><div class=\"ui-bar ui-bar-e\">"+msg.data.title+"</div></div>"
					+"<div class=\"ui-block-c\" style=\"height:45px;width:10%;\"><div class=\"ui-bar ui-bar-e\">"+timeconvert(msg.data.duration)+"</div></div></a>"
                                        +"<div class=\"ui-block-d\" style=\"height:45px;width:10%;\"><a href=\"#\" class=\"removebtn removebtn"+key+" ui-btn ui-shadow ui-corner-all ui-icon-delete ui-btn-icon-notext\"><div class=\"ui-bar ui-bar-e\">Delete</div></a></div>";
                               $("#searchlistgrid").append($newsearchsong)
                               $(".newaddsong"+key).click(function() {
                                    $.ajax({
                                        type: "GET",
                                        url: "/resources/playlist/add"+location.search+"&v="+o.id.videoId
                                    }).done(function( msg ) {
                                        playlist.push(o.id.videoId);
                                        key = playlist.length - 1;
                                         $.ajax({
                                            type: "GET",
                                            url: "http://gdata.youtube.com/feeds/api/videos/"+o.id.videoId+"?v=2&alt=jsonc"
                                        }).done(function( msg ) {
                                             $("#playlistgrid").append("<a class=\"newsong"+key+"\" href=\"#\"><div class=\"ui-block-a\" style=\"height:45px;width:15%;\"><div class=\"ui-bar ui-bar-e\"><img style=\"height:40px\" src='"+msg.data.thumbnail.sqDefault+"'/></div></div>"
                                                        +"<div class=\"ui-block-b\" style=\"height:45px;width:63%;\"><div class=\"ui-bar ui-bar-e\">"+msg.data.title+"</div></div>"
                                                        +"<div class=\"ui-block-c\" style=\"height:45px;width:10%;\"><div class=\"ui-bar ui-bar-e\">"+timeconvert(msg.data.duration)+"</div></div></a>"
                                                        +"<div class=\"ui-block-d\" style=\"height:45px;width:10%;\"><a href=\"#\" class=\"removebtn removebtn"+key+" ui-btn ui-shadow ui-corner-all ui-icon-delete ui-btn-icon-notext\"><div class=\"ui-bar ui-bar-e\">Delete</div></a></div>");
                                             $(".newsong"+key).click(function() {
                                                player.loadVideoById(playlist[key]);
                                                activesongnum = key;
                                             });
                                             $(".removebtn"+key).click(function() {
                                               var orderid = key+1
                                               console.log("o"+key);
                                                $.ajax({
                                                    type: "GET",
                                                    url: "/resources/playlist/remove"+location.search+"&o="+orderid
                                                }).done(function( msg ) {
                                                    noplaylist.push(key);
                                                    $(".newsong"+key).remove();
                                                    $(".removebtn"+key).remove();
                                                    if(activesongnum == key) {
                                                        activesongnum++;
                                                        while(noplaylist.indexOf(activesongnum) != -1) {
                                                            if(playlist.length > activesongnum ) {
                                                                activesongnum++;
                                                            }
                                                        }
                                                        if(playlist.length > activesongnum ) {
                                                            player.loadVideoById(playlist[activesongnum])
                                                        }
                                                    }
                                                });
                                            });
                                        });
                                    });
                                });
                            });
                            });
                        });
                    }
                });
            });


            var tag = document.createElement('script');

            tag.src = "https://www.youtube.com/iframe_api";
            var firstScriptTag = document.getElementsByTagName('script')[0];
            firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

            var player;

            var activesongnum;
            function onYouTubeIframeAPIReady() {
                $.ajax({
                    type: "GET",
                    url: "/resources/playlist/get"+location.search
                }).done(function( msg ) {
                    console.log(msg);
                    playlist = msg;


                    showplaylist("#playlist");

                    player = new YT.Player('player', {
                        height: '390',
                        width: '640',
                        videoId: playlist[0],
                        events: {
                            'onReady': onPlayerReady,
                            'onStateChange': onPlayerStateChange
                        }
                    });
                    activesongnum = 0;
                });

            }

            function onPlayerReady(event) {
                event.target.playVideo();
            }

            function onPlayerStateChange(event) {
                if (event.data == YT.PlayerState.ENDED) {
                    activesongnum++;
                    while(noplaylist.indexOf(activesongnum) != -1) {
                        if(playlist.length > activesongnum ) {
                            activesongnum++;
                        }
                    }
                    if(playlist.length > activesongnum ) {
                        player.loadVideoById(playlist[activesongnum])
                    }
                }
            }
            function stopVideo() {
                player.stopVideo();
            }

         