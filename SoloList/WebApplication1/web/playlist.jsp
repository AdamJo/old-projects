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
        <script type="text/javascript" src="/playlist.js"></script>

        <% 
          try {
                    Class.forName("com.mysql.jdbc.Driver"); // Initialize the driver
                    Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test?"
			                    + "user=root&password=admin");
                    System.out.println("connection Established");
                    ResultSet rs = con.createStatement().executeQuery("SELECT title, username FROM test.playlist where idplaylist = '"+request.getParameter("p")+"';");
                    String owner = "";
                    String title = "";
                    while (rs.next()) {
                        owner = rs.getString("username");
                        title = rs.getString("title");
                    }
                    if (!owner.equals(session.getAttribute( "username" ))) {
               
         %>
        <style>
            #addsongbtn {
                display: none;
            }
            .removebtn {
                display: none;
            }
            #loggedindiv {
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
            <div data-role="header"><h1><%= title %> by <a href="/user.jsp?u=<%= owner%>" data-ajax="false"><%= owner%></a></h1></div>
            <% }
    		catch (ClassNotFoundException e) {
                    e.printStackTrace();
		} catch (SQLException e) {
                    e.printStackTrace();
		}%>
            <div style="margin: 0 auto; width:640px">
                <div id="player"></div>
            </div>
            <div id="bottompart" style="min-height: 300px">
                 
            <div id="playlist">
           
            </div>
            <a id="addsongbtn" href="#searchpopup" data-role="button" data-rel="popup">Add Songs to Playlist</a>
            <div data-role="popup" id="searchpopup" data-position-to="#bottompart">
               <label for="basic">Search Songs:</label>
                <input type="text" name="name" id="searchtext" value="">
                <div id="searchlist" style="min-height: 200px">

                </div>
            </div>
            </div>
        </div>
    </body>
</html>
