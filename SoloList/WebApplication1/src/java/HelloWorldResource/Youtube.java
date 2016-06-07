/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package HelloWorldResource;

import com.google.api.client.googleapis.json.GoogleJsonResponseException;
import com.google.api.client.http.HttpRequest;
import com.google.api.client.http.HttpRequestInitializer;
import com.google.api.services.youtube.YouTube;
import com.google.api.services.youtube.model.SearchListResponse;
import com.google.api.services.youtube.model.SearchResult;
import samples.Auth;
import java.io.IOException;
import java.sql.SQLException;
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
@Path("youtube")
public class Youtube {

    private static final String apiKey = "AIzaSyBMrLaij-t7wFidH237zPAVCrP04Dqgzzs";

    private static final long NUMBER_OF_VIDEOS_RETURNED = 10;

     /**
     * Method handling HTTP GET requests. The returned object will be sent
     * to the client as "text/plain" media type.
     * @throws SQLException
     */
    @GET
    @Path("/search")
    @Produces(MediaType.APPLICATION_JSON)
    public List<SearchResult> search(@QueryParam("keyword") String keyword) {

        List<SearchResult> searchResultList = null;
        try {
            YouTube youtube = new YouTube.Builder(Auth.HTTP_TRANSPORT, Auth.JSON_FACTORY, new HttpRequestInitializer() {
                public void initialize(HttpRequest request) throws IOException {
                }
            }).setApplicationName("youtube-cmdline-search-sample").build();

            YouTube.Search.List search = youtube.search().list("id,snippet");
            search.setKey(apiKey);
            search.setQ(keyword);

            search.setType("video");

          //  search.setOrder("viewCount");
            
            search.setFields("items(id/kind,id/videoId,snippet/title,snippet/thumbnails/default/url)");
            search.setMaxResults(NUMBER_OF_VIDEOS_RETURNED);

            SearchListResponse searchResponse = search.execute();
            searchResultList = searchResponse.getItems();

        } catch (GoogleJsonResponseException e) {
            System.err.println("There was a service error: " + e.getDetails().getCode() + " : "
                    + e.getDetails().getMessage());
        } catch (IOException e) {
            System.err.println("There was an IO error: " + e.getCause() + " : " + e.getMessage());
        } catch (Throwable t) {
            t.printStackTrace();
        }
        return searchResultList;
    }
}
