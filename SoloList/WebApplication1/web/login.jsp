<%@ page import="java.sql.*, com.apress.jdbc.*" %>
<html>
  <head>
          <%
    PreparedStatement stmt = null;
    try {
      Class.forName("com.mysql.jdbc.Driver"); // Initialize the driver
                    Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test?"
			                    + "user=root&password=admin");
                      System.out.println("connection Established");
       ResultSet rs = con.createStatement().executeQuery("SELECT username FROM test.users where username = '"+request.getParameter( "username" )+"' and password = '"+request.getParameter( "pass" )+"';");

      if (rs.next()) {
          session.setAttribute( "username", request.getParameter( "username" ) );
%>
    <meta http-equiv="refresh" content="0; url=/user.jsp?u=<%= session.getAttribute( "username" ) %>" />
</head>
  <body>
 
<%
      } else {
%>
    <meta http-equiv="refresh" content="0; url=/login.html" />
</head>
  <body>
<%
      }
    } catch (SQLException e) {
%>
    <%= e.getMessage() %>

<%
      e.printStackTrace();
    } 
%>
  </body>
</html>