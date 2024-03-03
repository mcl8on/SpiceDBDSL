


from lark import Lark

spicedb_parser =  Lark(r"""
                       
    value: object+
                       

    object: "definition" object_name "{" def* "}" 
    def: relation* | permission*
    relation: "relation" role ":" obj
    permission: "permission" permission_name "=" perm_expr
                       
    perm_expr: role (perm_ops role)*
            | "(" perm_expr  ")"
            | perm_expr (perm_ops perm_expr)*      
                       
                                     
    role: CNAME
    obj: CNAME  
    permission_name: CNAME 
    object_name: CNAME

    perm_ops: "+"|"-"|"&"|"|"               

    COMMENT: /#[^\n]*/
    MULTILINE_COMMENT: /\/\*(\*(?!\/)|[^*])*\*\//
 
    %import common.CNAME
    %import common.WS
    %ignore WS
    %ignore COMMENT        
    %ignore MULTILINE_COMMENT         

                       
""", start='value')


with open("t.schema") as f:
    data = f.read()
     
print (spicedb_parser.parse(data).pretty())


                       

