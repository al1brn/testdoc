from docutils import nodes
from docutils.parsers.rst import Directive, directives

#for k in dir(nodes):
#    print(k)
    
#print(help(nodes.reference))

class HelloWorld(Directive):
    
    has_content = True
    
    def run(self):
        
        blid = self.content[0]
        
        
        para = nodes.subscript(text="Blender reference : ")

        text = f"{blid} API, "
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
        
        return [para]
        
        blid = self.content[0]
        url = f'<a href="https://docs.blender.org/api/current/bpy.types.{self.content[0]}.html">{blid} Blender reference</a>'
        
        return [nodes.reference('', 'text')] #, internal=False, refuri="https://google.com")]
        
        paragraph_node = nodes.paragraph(text=url)
        return [paragraph_node]


def setup(app):

    app.add_directive("blid", HelloWorld)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }