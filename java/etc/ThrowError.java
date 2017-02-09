import  java.lang.*;


public class ThrowError
{  
    public static void main(String [] args)  throws Exception
    {
        try {
            badMethod();  
            System.out.print("A"); 
        }  
        catch (Exception ex) {
            System.out.print("B");  
        } 
        finally {
            System.out.print("C"); 
        } 

        System.out.print("D"); 
    }  
    public static void badMethod()  throws Exception {
        // throw new Error(); /* Line 22 */
        Exception e = new Exception();
        throw e;        
    } 
}