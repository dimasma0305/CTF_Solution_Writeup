const graphql = (query, variables) => { 
    let r;
    if (variables) {
        r = (
            JSON.stringify(
            variables,
            )
        );
    }
    return r
  };

let res = graphql(`
mutation($username: String!, $password: String!) { 
  login(username: $username, password: $password) { 
    username 
  } 
}
`,
{
    "password":"testing_urename",
    "useraname":"testing_password",
});

console.log(res)