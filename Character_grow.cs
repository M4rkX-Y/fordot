using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Character_grow : MonoBehaviour
{

    public float speed = 1f;
    public float delay = 4.5f;
    public float bsize = 1f;
    private int stop = 0;
    private float time;
    private bool up = true;
    public Vector2 t;
    public Vector2 f;
    public Vector2 b;
    public Vector2 s;

    // Start is called before the first frame update
    void Start()
    {
        f = transform.localScale;
        b.x = f.x + bsize;
        b.y = f.x + bsize;
    }

    // Update is called once per frame
    void Update()
    {
        time = delay/transform.localScale.x;
        if (stop==0) {
            Invoke("stay", time);            
        }
        
        if (stop==1) {
            Invoke("big", time);            
        }

        if (stop==2) {
            Invoke("small", time);
        }
        
        if (Input.GetKeyUp("escape")) {
            b.x = f.x + bsize;
            b.y = f.x + bsize;
            stop = 0;
        }

        if (Input.GetKeyUp("space")) {
            stop = 1;
        }
     
        if (Input.GetKeyUp(KeyCode.Return)) {
            stop = 2;
        }
            
    }
    void big(){
        t = transform.localScale;
        if (t.x < 5) {
            t.x += Time.deltaTime * speed;
            t.y += Time.deltaTime * speed;
            transform.localScale = t;
        }
    }
    void stay(){
        f = transform.localScale;
        transform.localScale = f;

            
    }
    void small(){
        s = transform.localScale;
        if (s.x > 2) {
            s.x += Time.deltaTime * speed * -1;
            s.y += Time.deltaTime * speed * -1;
            transform.localScale = s;
        }
    }
}
