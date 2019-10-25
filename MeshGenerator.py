from os.path import join, dirname


class MeshGenerator:
    def __init__(self):
        self.curve_it = 0
        self.colors = ["#c0392b", " #2980b9", "#27ae60"]
        self.three_path = join(dirname(__file__), "js/three.js")
        self.Detector_path = join(dirname(__file__), "js/Detector.js")
        self.OrbitControls_path = join(dirname(__file__), "js/OrbitControls.js")
        self.OBJLoader_path = join(dirname(__file__), "js/OBJLoader.js")
        self.MTLLoader_path = join(dirname(__file__), "js/MTLLoader.js")
        self.event_listener = []
        self.added_mesh = []


    def make_header(self):
        ret_str = ""
        js_libs = [self.three_path ,self.Detector_path, self.OrbitControls_path, self.OBJLoader_path, self.MTLLoader_path]
        print(js_libs)
        for file in js_libs:
            with open(file, "r") as js_file:
                print(file)
                ret_str += "  <script type=\"text/javascript\">\n  " + js_file.read().replace("\n", "\n  ") + " \n</script>\n"
        return ret_str

    def make_mesh(self, mesh_path, title=None):
        out_string = f"<div id=\"mesh_{self.curve_it}\"> <h4>{title}</h4> </div>\n"

        out_string += "     <script>\n"
        out_string += "     if (!Detector.webgl) {\nDetector.addGetWebGLMessage();\n}\n"
        init_function = ""
        init_function += "     var my_mesh;\nvar objLoader_my_mesh;\n"
        init_function += "     var camera_my_mesh, controls_my_mesh, scene_my_mesh, renderer_my_mesh;\n"
        init_function += "     var lighting, ambient, keyLight_my_mesh, fillLight_my_mesh, backLight_my_mesh;\n"
        init_function += "     var windowX = 400;\nvar windowY = 250;\n"
        init_function += "     init_my_mesh();\nanimate_my_mesh();\n"

        init_function += "\n\
            function init_my_mesh() {\n\
                my_mesh = document.getElementById('my_mesh');\n\
                /* Camera */\n\
                camera_my_mesh = new THREE.PerspectiveCamera(10, 1, 0.1, 2500);\n\
                camera_my_mesh.position.set( 5, 5, -10 );\n\
                /* Scene */\n\
                scene_my_mesh = new THREE.Scene();\n\
                lighting = true;\n\
                ambient_my_mesh = new THREE.AmbientLight(0xffffff, 0.15);\n\
                scene_my_mesh.add(ambient_my_mesh);\n\
                keyLight_my_mesh = new THREE.DirectionalLight(0xffffff, 0.15);\n\
                keyLight_my_mesh.position.set(-100, 0, 100);\n\
                fillLight_my_mesh = new THREE.DirectionalLight(0xffffff, 0.15);\n\
                fillLight_my_mesh.position.set(100, 0, 100);\n\
                fillLight1_my_mesh = new THREE.DirectionalLight(0xffffff, 0.15);\n\
                fillLight2_my_mesh = new THREE.DirectionalLight(0xffffff, 0.15);\n\
                fillLight3_my_mesh = new THREE.DirectionalLight(0xffffff, 0.15);\n\
                fillLight4_my_mesh = new THREE.DirectionalLight(0xffffff, 0.15);\n\
                backLight_my_mesh = new THREE.DirectionalLight(0xffffff, 1.0);\n\
                backLight_my_mesh.position.set(100, 0, -100).normalize();\n\
                scene_my_mesh.position.set( -0.25,-0.25,0 );\n\
                scene_my_mesh.add(keyLight_my_mesh, fillLight_my_mesh, backLight_my_mesh , fillLight1_my_mesh, fillLight2_my_mesh, fillLight3_my_mesh, fillLight4_my_mesh);\n\
                /* Model */\n\
                objLoader_my_mesh = new THREE.OBJLoader();\n\
                objLoader_my_mesh.load('output_atlas.obj', function (object) {\n\
                    object.name = 'object';\n\
                    scene_my_mesh.add(object);\n\
                });\n\
                /* Renderer */\n\
                renderer_my_mesh = new THREE.WebGLRenderer();\n\
                renderer_my_mesh.setPixelRatio(window.devicePixelRatio);\n\
                renderer_my_mesh.setSize(windowX, windowY);\n\
                renderer_my_mesh.setClearColor(new THREE.Color(\"hsl(0%, 0%, 83%)\"));\n\
                my_mesh.appendChild(renderer_my_mesh.domElement);\n\
                /* Controls */\n\
                controls_my_mesh = new THREE.OrbitControls(camera_my_mesh, renderer_my_mesh.domElement);\n\
                controls_my_mesh.enableDamping = true;\n\
                controls_my_mesh.dampingFactor = 0.25;\n\
                controls_my_mesh.enableZoom = false;\n\
                /* Events */\n\
                }\
                "



        init_function += "\n\
            function animate_my_mesh() {\n\
                requestAnimationFrame(animate_my_mesh);\n\
                controls_my_mesh.update();\n\
                render_my_mesh();\n\
                }\n\
            "

        init_function += "\n\
            function render_my_mesh() {\n\
                renderer_my_mesh.render(scene_my_mesh, camera_my_mesh);\n\
                }\n\
             "

        init_function = init_function.replace("my_mesh", "mesh_" + str(self.curve_it))
        self.added_mesh.append("mesh_" + str(self.curve_it))
        out_string += init_function

        out_string += "</script>\n"

        self.curve_it += 1

        return out_string

    def make_onWindowResize(self):
        self.event_listener.append("\
            window.addEventListener('resize', onWindowResize, false);\n\
            window.addEventListener('keydown', onKeyboardEvent, false);\n\
            \n\
            ")

        onWindowResize = "\n\
                function onWindowResize() {\n\
                 "

        for mesh_id in self.added_mesh:
            local_str = f"camera_my_mesh.aspect = windowX / windowY;\n\
                    camera_my_mesh.updateProjectionMatrix();\n\
                    renderer_my_mesh.setSize(windowX, windowY);\n "
            onWindowResize += local_str.replace("my_mesh", mesh_id)
        onWindowResize += " }\n "
        self.event_listener.append(onWindowResize)

    def make_init_function(self):
        init_function = "\n\
            function onKeyboardEvent(e) {\n\
                if (e.code === 'KeyL') {\n\
                    lighting = !lighting;\n\
                    if (lighting) {\n\
                "

        for mesh_id in self.added_mesh:
            local_str = "ambient_my_mesh.intensity = 0.25;\n\
                        scene_my_mesh.add(keyLight_my_mesh);\n\
                        scene_my_mesh.add(fillLight_my_mesh);\n\
                        scene_my_mesh.add(fillLight1_my_mesh);\n\
                        scene_my_mesh.add(fillLight2_my_mesh);\n\
                        scene_my_mesh.add(fillLight3_my_mesh);\n\
                        scene_my_mesh.add(fillLight4_my_mesh);\n\
                        scene_my_mesh.add(backLight_my_mesh);\n"
            init_function += local_str.replace("my_mesh", mesh_id)

        init_function += " } else {\n\
                    "

        for mesh_id in self.added_mesh:
            local_str = "ambient_my_mesh.intensity = 1.0;\n\
                        scene_my_mesh.remove(keyLight_my_mesh);\n\
                        scene_my_mesh.remove(fillLight_my_mesh);\n\
                        scene_my_mesh.remove(fillLight1_my_mesh);\n\
                        scene_my_mesh.remove(fillLight2_my_mesh);\n\
                        scene_my_mesh.remove(fillLight3_my_mesh);\n\
                        scene_my_mesh.remove(fillLight4_my_mesh);\n\
                        scene_my_mesh.remove(backLight_my_mesh);\n"
            init_function += local_str.replace("my_mesh", mesh_id)

        init_function += "        }\n\
                }\n\
                }\n\
            "
        self.event_listener.append(init_function)

    def end_mesh(self):
        self.event_listener.append("<script>\n")
        self.make_onWindowResize()
        self.make_init_function()
        self.event_listener.append("</script>\n")
        return "".join(self.event_listener)
