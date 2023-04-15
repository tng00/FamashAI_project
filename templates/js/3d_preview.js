import * as THREE from 'three';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';
import {OBJLoader} from 'three/addons/loaders/OBJLoader.js';
// import {MTLLoader} from 'three/addons/loaders/MTLLoader.js';

function main() {
	const canvas = document.querySelector('#c');
	const renderer = new THREE.WebGLRenderer({alpha: true, canvas});
	renderer.outputEncoding = THREE.sRGBEncoding;

	const fov = 45;
	const aspect = 2;
	const near = 0.1;
	const far = 10000;
	const camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
	camera.position.set(0, 30, 460);

	const controls = new OrbitControls(camera, canvas);
	controls.target.set(0, 5, 0);
	controls.enablePan = false;
	controls.update();

	const scene = new THREE.Scene();

	{
		const color = 0xFFFFFF;
		const intensity = 0.15;
		const light = new THREE.AmbientLight(color, intensity);
		scene.add(light);
	}

	{
		const color = 0xFFFFFF;
		const intensity = 0.4;
		const light_1 = new THREE.DirectionalLight(color, intensity);
		light_1.position.set(0, 200, 460);
		scene.add(light_1);
	}

	{
		const color = 0xFFFFFF;
		const intensity = 0.2;
		const light_2 = new THREE.DirectionalLight(color, intensity);
		light_2.position.set(0, 200, -460);
		scene.add(light_2);
	}

	{
		const material = new THREE.MeshPhongMaterial({
			color: 0xbebebe,
			side: THREE.DoubleSide
		});
		const objLoader = new OBJLoader();
		objLoader.load('templates/obj models/5-36/5-36-in_mesh.obj', (root) => {
		// objLoader.load('obj models/6-45/6-45-in_mesh.obj', (root) => {
			root.traverse(node => {
				node.material = material;
			})
			scene.add(root);
			root.position.set(-200, -195, -120)
		});
	}

	function resizeRendererToDisplaySize(renderer) {
		const canvas = renderer.domElement;
		const width = canvas.clientWidth * 1.5;
		const height = canvas.clientHeight * 1.5;
		const needResize = canvas.width !== width || canvas.height !== height;
		if (needResize) {
			renderer.setSize(width, height, false);
		}
		return needResize;
	}

	function render() {

		if (resizeRendererToDisplaySize(renderer)) {
			const canvas = renderer.domElement;
			camera.aspect = canvas.clientWidth / canvas.clientHeight;
			camera.updateProjectionMatrix();
		}

		renderer.render(scene, camera);

		requestAnimationFrame(render);
	}

	requestAnimationFrame(render);
}

main();
