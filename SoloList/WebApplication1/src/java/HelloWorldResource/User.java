package HelloWorldResource;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;

/**
 * Root resource (exposed at "myresource" path)
 */
@Path("user")
public class User {

    /**
     * Method handling HTTP GET requests. The returned object will be sent
     * to the client as "text/plain" media type.
     * @throws SQLException
     */
    @GET
    @Path("/new")
    @Produces(MediaType.APPLICATION_JSON)
    public Boolean getIt(@QueryParam("name") String name) throws SQLException {

    	Boolean b = false;
		try {
                     Class.forName("com.mysql.jdbc.Driver"); // Initialize the driver
                    Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test?"
			                    + "user=root&password=admin");
                    System.out.println("connection Established");
                    ResultSet rs = con.createStatement().executeQuery("SELECT count(user_id) as rows FROM users");
                    String numrows = "";
                    while (rs.next() == true){
                        numrows = rs.getString("rows");
                    }
                    con.createStatement().execute("INSERT INTO users (user_id, username) VALUES ('"+numrows+"', '"+name+"')"); //Insert a row
                    b = true;
			}
    		catch (ClassNotFoundException e) {
                    e.printStackTrace();
		} catch (SQLException e) {
                    e.printStackTrace();
		}
		return b;
    }
}
