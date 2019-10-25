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
        out_string += "     var my_mesh;\nvar objLoader;\n"
        out_string += "     var camera, controls, scene, renderer;\n"
        out_string += "     var lighting, ambient, keyLight, fillLight, backLight;\n"
        out_string += "     var windowX = 400;\nvar windowY = 250;\n"
        out_string += "     init();\nanimate();\n"

        init_function = "\n\
            function init() {\n\
                my_mesh = document.getElementById('my_mesh');\n\
                /* Camera */\n\
                camera = new THREE.PerspectiveCamera(10, 1, 0.1, 2500);\n\
                camera.position.set( 5, 5, -10 );\n\
                /* Scene */\n\
                scene = new THREE.Scene();\n\
                lighting = true;\n\
                ambient = new THREE.AmbientLight(0xffffff, 0.15);\n\
                scene.add(ambient);\n\
                keyLight = new THREE.DirectionalLight(0xffffff, 0.15);\n\
                keyLight.position.set(-100, 0, 100);\n\
                fillLight = new THREE.DirectionalLight(0xffffff, 0.15);\n\
                fillLight.position.set(100, 0, 100);\n\
                fillLight1 = new THREE.DirectionalLight(0xffffff, 0.15);\n\
                fillLight.position.set(100, 50, 100);\n\
                fillLight2 = new THREE.DirectionalLight(0xffffff, 0.15);\n\
                fillLight.position.set(100, -50, 100);\n\
                fillLight3 = new THREE.DirectionalLight(0xffffff, 0.15);\n\
                fillLight.position.set(100, 50, -100);\n\
                fillLight4 = new THREE.DirectionalLight(0xffffff, 0.15);\n\
                fillLight.position.set(100, -50, -100);\n\
                backLight = new THREE.DirectionalLight(0xffffff, 1.0);\n\
                backLight.position.set(100, 0, -100).normalize();\n\
                scene.position.set( -0.25,-0.25,0 );\n\
                scene.add(keyLight, fillLight, backLight , fillLight1, fillLight2, fillLight3, fillLight4);\n\
                /* Model */\n\
                objLoader = new THREE.OBJLoader();\n\
                objLoader.load('output_atlas.obj', function (object) {\n\
                    object.name = 'object';\n\
                    scene.add(object);\n\
                });\n\
                /* Renderer */\n\
                renderer = new THREE.WebGLRenderer();\n\
                renderer.setPixelRatio(window.devicePixelRatio);\n\
                renderer.setSize(windowX, windowY);\n\
                renderer.setClearColor(new THREE.Color(\"hsl(5, 0%, 70%)\"));\n\
                my_mesh.appendChild(renderer.domElement);\n\
                /* Controls */\n\
                controls = new THREE.OrbitControls(camera, renderer.domElement);\n\
                controls.enableDamping = true;\n\
                controls.dampingFactor = 0.25;\n\
                controls.enableZoom = false;\n\
                /* Events */\n\
                window.addEventListener('resize', onWindowResize, false);\n\
                window.addEventListener('keydown', onKeyboardEvent, false);\n\
                }\n\
            "

        init_function = init_function.replace("my_mesh", "mesh_" + str(self.curve_it))
        out_string += init_function

        out_string += "\n\
            function onWindowResize() {\n\
                camera.aspect = windowX / windowY;\n\
                camera.updateProjectionMatrix();\n\
                renderer.setSize(windowX, windowY);\n\
                }\n\
            "

        out_string += "\n\
            function onKeyboardEvent(e) {\n\
                if (e.code === 'KeyL') {\n\
                    lighting = !lighting;\n\
                    if (lighting) {\n\
                        ambient.intensity = 0.25;\n\
                        scene.add(keyLight);\n\
                        scene.add(fillLight);\n\
                        scene.add(backLight);\n\
                    } else {\n\
                        ambient.intensity = 1.0;\n\
                        scene.remove(keyLight);\n\
                        scene.remove(fillLight);\n\
                        scene.remove(backLight);\n\
                    }\n\
                }\n\
                }\n\
            "

        out_string += "\n\
            function animate() {\n\
                requestAnimationFrame(animate);\n\
                controls.update();\n\
                render();\n\
                }\n\
            "

        out_string += "\n\
            function render() {\n\
                renderer.render(scene, camera);\n\
                }\n\
             "

        out_string += "</script>\n"

        self.curve_it += 1

        return out_string
