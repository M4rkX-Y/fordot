using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Switch : MonoBehaviour
{

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyUp("space"))
        {
            Water2D.Water2D_Spawner.instance.Spawn();
        }

        if (Input.GetKeyUp("escape"))
        {
            Water2D.Water2D_Spawner.instance._breakLoop = true;
        }
        
        if (Input.GetKeyUp(KeyCode.Return)) {
            Water2D.Water2D_Spawner.instance.Spawn();
        }
    }
}
