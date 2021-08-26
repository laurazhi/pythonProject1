package api;

import org.testng.annotations.Test;

import com.google.gson.JsonObject;

import static io.restassured.RestAssured.*;

public class dexcom_Api {
	private static final String JSON = "application/json";
	String baseUrl = "https://clarity.dexcom.com/api/";
	
	private String getEndpoint(String endpoint) {
		return baseUrl + endpoint;
	}
	
	@Test
	public void verifyPostTokenReturnValue() {
		String endpoint = getEndpoint("subject/168127779457576550/analysis_session");
		//String token = "QpwL5tke4Pnpja7X4";

		JsonObject loginCredentials = new JsonObject();
		loginCredentials.addProperty("username", "codechallenge");
		loginCredentials.addProperty("password", "Password123");

		given()
		.contentType(JSON)
		.body(loginCredentials.toString())
		.post(endpoint)
		.then()
		.assertThat()
		.statusCode(404)
		.and();
		//.body("sessionID",null);			
	}
}