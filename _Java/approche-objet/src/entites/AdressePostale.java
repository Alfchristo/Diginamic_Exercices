package entites;

public class AdressePostale {
    public int numRue;
    public String libelleRue;
    public int codePostal;
    public String ville;  // TP 1

    public AdressePostale(int nvRue, String nvLibRue, int nvCPostal, String nvVille){
        numRue = nvRue;
        libelleRue = nvLibRue;
        codePostal = nvCPostal;
        ville = nvVille;
    }
}
