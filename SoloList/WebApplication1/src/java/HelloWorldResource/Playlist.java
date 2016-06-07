/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package HelloWorldResource;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;


/**
 *
 * @author Evan
 */
@Path("playlist")
public class Playlist {

     /**
     * Method handling HTTP GET requests. The returned object will be sent
     * to the client as "text/plain" media type.
     * @throws SQLException
     */
    @GET
    @Path("/get")
    @Produces(MediaType.APPLICATION_JSON)
    public List<String> getIt(@QueryParam("p") String playlist) throws SQLException {

        List<String> list = new ArrayList<String>();
                try {
                    Class.forName("com.mysql.jdbc.Driver"); // Initialize the driver
                    Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test?"
			                    + "user=root&password=admin");
                    System.out.println("connection Established");
                    ResultSet rs = con.createStatement().executeQuery("SELECT videoid FROM test.playlistsong where idplaylist = '"+playlist+"' order by orderid;");
                    String numrows = "";
                    while (rs.next() == true){
                        list.add(rs.getString("videoid"));
                    }
                }
    		catch (ClassNotFoundException e) {
                    e.printStackTrace();
		} catch (SQLException e) {
                    e.printStackTrace();
		}
		return list;
    }

    @GET
    @Path("/add")
    @Produces(MediaType.APPLICATION_JSON)
    public List<String> add(@QueryParam("p") String playlist, @QueryParam("v") String video) throws SQLException {

        List<String> list = new ArrayList<String>();
                try {
                    Class.forName("com.mysql.jdbc.Driver"); // Initialize the driver
                    Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test?"
			                    + "user=root&password=admin");
                    System.out.println("connection Established");
                    ResultSet rs = con.createStatement().executeQuery("SELECT count(*) FROM test.playlistsong where idplaylist ="+playlist+";");
                    int numrows = 0;
                    while (rs.next()) {
                        numrows = rs.getInt(1);
                    }
                    numrows++;
                     con.createStatement().execute("INSERT INTO playlistsong (idplaylist, videoid, orderid) VALUES ('"+playlist+"', '"+video+"', "+numrows+");"); //Insert a row

                }
    		catch (ClassNotFoundException e) {
                    e.printStackTrace();
		} catch (SQLException e) {
                    e.printStackTrace();
		}
		return list;
    }

    @GET
    @Path("/remove")
    @Produces(MediaType.APPLICATION_JSON)
    public boolean remove(@QueryParam("p") String playlist, @QueryParam("o") String orderid) throws SQLException {

        List<String> list = new ArrayList<String>();
                try {
                    Class.forName("com.mysql.jdbc.Driver"); // Initialize the driver
                    Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test?"
			                    + "user=root&password=admin");
                    System.out.println("connection Established");
                    con.createStatement().execute("DELETE FROM playlistsong where idplaylist='"+playlist+"' and orderid='"+orderid+"';"); //delete a row
                    con.createStatement().execute("UPDATE playlistsong SET orderid = orderid-1 where idplaylist='"+playlist+"' and orderid>='"+orderid+"';"); //delete a row

                }
    		catch (ClassNotFoundException e) {
                    e.printStackTrace();
		} catch (SQLException e) {
                    e.printStackTrace();
		}
		return true;
    }

    @GET
    @Path("/removelist")
    @Produces(MediaType.APPLICATION_JSON)
    public boolean removelist(@QueryParam("p") String playlist) throws SQLException {

                try {
                    Class.forName("com.mysql.jdbc.Driver"); // Initialize the driver
                    Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test?"
			                    + "user=root&password=admin");
                    System.out.println("connection Established");
                    con.createStatement().execute("UPDATE playlist SET username = 'TestAccount1' where idplaylist='"+playlist+"';"); //delete a row

                }
    		catch (ClassNotFoundException e) {
                    e.printStackTrace();
		} catch (SQLException e) {
                    e.printStackTrace();
		}
		return true;
    }

    @GET
    @Path("/rename")
    @Produces(MediaType.APPLICATION_JSON)
    public boolean rename(@QueryParam("p") String playlist, @QueryParam("t") String title) throws SQLException {

                try {
                    Class.forName("com.mysql.jdbc.Driver"); // Initialize the driver
                    Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test?"
			                    + "user=root&password=admin");
                    System.out.println("connection Established");
                    con.createStatement().execute("UPDATE playlist SET title = '"+title+"' where idplaylist='"+playlist+"';"); //delete a row

                }
    		catch (ClassNotFoundException e) {
                    e.printStackTrace();
		} catch (SQLException e) {
                    e.printStackTrace();
		}
		return true;
    }

    @GET
    @Path("/new")
    @Produces(MediaType.APPLICATION_JSON)
    public int newPlay(@QueryParam("u") String user) throws SQLException {
            int numrows = 0;
                try {
                    Class.forName("com.mysql.jdbc.Driver"); // Initialize the driver
                    Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test?"
			                    + "user=root&password=admin");
                    System.out.println("connection Established");
                    ResultSet rs = con.createStatement().executeQuery("SELECT count(*) FROM test.playlist;");
                  
                    while (rs.next()) {
                        numrows = rs.getInt(1);
                    }
                    numrows++;
                     con.createStatement().execute("INSERT INTO playlist (idplaylist, title, username) VALUES ('"+numrows+"', 'New Playlist', '"+user+"')"); //Insert a row

                }
    		catch (ClassNotFoundException e) {
                    e.printStackTrace();
		} catch (SQLException e) {
                    e.printStackTrace();
		}
		return numrows;
    }

    @GET
    @Path("/playlists")
    @Produces(MediaType.APPLICATION_JSON)
    public  ArrayList<ArrayList<String>> getPlaylists(@QueryParam("u") String user) throws SQLException {
            ArrayList<ArrayList<String>> playlistlist = new ArrayList<ArrayList<String>>();
                try {
                    Class.forName("com.mysql.jdbc.Driver"); // Initialize the driver
                    Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test?"
			                    + "user=root&password=admin");
                    System.out.println("connection Established");
                    ResultSet rs = con.createStatement().executeQuery("SELECT title, idplaylist FROM test.playlist where username = '"+user+"';");
                    while (rs.next()) {
                        ArrayList<String> playlist = new ArrayList<String>();
                        playlist.add(rs.getString("idplaylist"));
                        playlist.add(rs.getString("title"));
                        playlistlist.add(playlist);
                    }
                }
    		catch (ClassNotFoundException e) {
                    e.printStackTrace();
		} catch (SQLException e) {
                    e.printStackTrace();
		}
		return playlistlist;
    }


}