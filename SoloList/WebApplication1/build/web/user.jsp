<%@page import="java.sql.SQLException"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.Connection"%>
<!--
To change this template, choose Tools | Templates
and open the template in the editor.
-->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
    <head>
        <title>SoloList</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="themes/main.min.css" />
		<link rel="stylesheet" href="themes/jquery.mobile.icons.min.css" />
		<link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.2/jquery.mobile.structure-1.4.2.min.css" />
		<script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
		<script src="http://code.jquery.com/mobile/1.4.2/jquery.mobile-1.4.2.min.js"></script>
                 <script type="text/javascript" src="/user.js"></script>
        <% 
                   if (!request.getParameter("u").equals(session.getAttribute( "username" ))) {
         %>
        <style>
            #addplaylistbtn, .editbtn, .removebtn, #loggedindiv {
                display: none;
            }
        </style>
               <% }
                    else {
                %>
                 <style>
                    #tologindiv {
                        display: none;
                    }
                 </style>
                <% }
                    %>
    </head>
    <body>
        <div data-role="page">
            <div id="tologindiv"><h1 role="heading" aria-level="1"><a href="/login.html" data-ajax="false" class="ui-link">login</a></h1></div>
            <div id="loggedindiv"><h1 role="heading" aria-level="1">Hello, <%= session.getAttribute( "username" )%></h1></div>
            <div data-role="header"><h1><%= request.getParameter("u")%>'s Playlists</h1></div><br/>
            <div id="playlist"></div>
            <a data-role="button" id="addplaylistbtn">Create new playlist</a>

        </div>
    </body>
</html>
