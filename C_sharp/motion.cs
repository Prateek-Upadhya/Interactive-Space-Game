using UnityEngine;


public class motion : MonoBehaviour
{
    float x_coordinate;
    float y_coordinate;
    public Rigidbody shuttle;
    public float forward_force = 2000f;
    public float horizontal_force = 100f;
    public float vertical_force = 50f;
    public UDPReceive dataReceive;
    //    public GameObject main_player
    void Update()
    {
        string data = dataReceive.data;
        data = data.Remove(0, 1);  //removes the bracket at the beginning
        data = data.Remove(data.Length - 1, 1); //removes the data at the end
        string[] point = data.Split(',');


        x_coordinate = float.Parse(point[0]);
        y_coordinate = float.Parse(point[1]);

 //       main_player.transform.position = new Vector3(x, y, 0);
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        shuttle.AddForce(0, 0, forward_force * Time.deltaTime);

        if (x_coordinate > 640)
        {
            shuttle.AddForce(horizontal_force * Time.deltaTime, 0, 0, ForceMode.VelocityChange);
        } else if( x_coordinate < 640)
        {
            shuttle.AddForce(-horizontal_force * Time.deltaTime, 0, 0, ForceMode.VelocityChange);
        }

        if (y_coordinate > 360)
        {
            shuttle.AddForce(0, vertical_force * Time.deltaTime, 0, ForceMode.VelocityChange);
        }
        else if (y_coordinate < 360)
        {
            shuttle.AddForce(0, -vertical_force * Time.deltaTime, 0, ForceMode.VelocityChange);
        }

       
}
}
