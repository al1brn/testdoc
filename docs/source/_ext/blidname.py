from docutils import nodes
from docutils.parsers.rst import Directive, directives

#for k in dir(nodes):
#    print(k)
    
#print(help(nodes.reference))

class Blidname(Directive):
    
    has_content = True
    
    def run(self):
        
        blid = self.content[0].strip()
        
        para = nodes.subscript(text="Blender reference : ")

        text = f"{blid}, "
        api_url = f"https://docs.blender.org/api/current/bpy.types.{self.content[0]}.html"
        
        refnode = nodes.reference('', '', internal=False, refuri=api_url)
        innernode = nodes.emphasis(text, text)
        refnode.append(innernode)
        para += refnode
        
        text = f"Node {blid}"
        api_url = f"https://docs.blender.org/api/current/bpy.types.{self.content[0]}.html"

        refnode = nodes.reference('', '', internal=False, refuri=api_url)
        innernode = nodes.emphasis(text, text)
        refnode.append(innernode)
        para += refnode
        
        para += nodes.paragraph('')
        
        return [para]




def setup(app):

    app.add_directive("blid", Blidname)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }