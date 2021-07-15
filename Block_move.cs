using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Block_move : MonoBehaviour
{
    // Start is called before the first frame update
    private Vector2 t;

    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        t = new Vector2(0.0f, 0.0f);

        if (Input.GetKeyUp("space")) {
            in_water();
        }
     
        if (Input.GetKeyUp(KeyCode.Return)) {
            out_water();
        }
    }
    void in_water() {
        t.y += -3;
        transform.position = t;
    }
    void out_water() {
        t.y += 4;
        transform.position = t;
    }
}
