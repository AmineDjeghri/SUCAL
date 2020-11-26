        let login       = document.getElementById('sign in');
        let name        = document.getElementById('name');
        let email       = document.getElementById('email');
        let password    = document.getElementById('password');
        let regname     = new RegExp("^[a-z0-9_-]{3,15}$");
        let regemail    = new RegExp("[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+");
        let regpassword = new RegExp("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$");
        login.disabled = true; 
        let check = () => {
            if(     
            (regemail.exec(email.value) === null || regemail.exec(email.value)[0] !== email.value) || 
            (regname.exec(name.value) === null  || regname.exec(name.value)[0] !== name.value   ) ||
            (regpassword.exec(password.value) === null || regpassword.exec(password.value)[0] !== password.value)
            )
            {
                    login.disabled = true; 
            }
            else
            {
                    login.disabled = false; 
            }
        }
        email.addEventListener("blur",(event)=>{
            if(regemail.exec(email.value) === null || regemail.exec(email.value)[0] !== email.value )
            {      
                   event.target.style.border="2px solid red"  
            }
            else
            {       
                    event.target.style.border="2px solid green"  
            }
            check()
        })

        name.addEventListener("blur",(event)=>{ 
            if(regname.exec(name.value) ===null  || regname.exec(name.value)[0] !== name.value )
            {       
                    name.style.border="2px solid red" 
                     
            }
            else 
            {       
                    event.target.style.border="2px solid green"  
            }
            check()
        })

        password.addEventListener("blur",(event)=>{  
            if(regpassword.exec(password.value) ===null || regpassword.exec(password.value)[0] !== password.value )
            {        
                    password.style.border="2px solid red";  
            }
            else
            {       
                    event.target.style.border="2px solid green"  
            }
            check()
        })
        